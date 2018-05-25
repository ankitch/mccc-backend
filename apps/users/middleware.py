from rest_framework_jwt.settings import api_settings

from apps.users.models import User, Role
from apps.users.serializers import RoleSerializer


def clear_roles(request):
    request.__class__.role = None
    request.__class__.company = None
    request.__class__.roles = []
    request.__class__.role_data = []
    return request


class RoleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('HTTP_AUTHORIZATION'):
            token_key = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
            payload = api_settings.JWT_DECODE_HANDLER(token_key)
            user_id = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER(payload)
            try:
                request.user = User.objects.get(pk=user_id)
                print(request.user)
            except User.DoesNotExist:
                pass

        role = None
        role_obj = None
        if request.user.is_authenticated:
            roles = request.user.all_roles
            try:
                role_obj = Role.objects.get(user=request.user.id)
            except Role.DoesNotExist:
                pass

            if role:
                role = next((role for role in roles if role.id == role_obj), None)
            if not role and roles:
                role = roles[0]
            if role:
                request.__class__.role = role
                request.__class__.company = role.company
                request.__class__.roles = roles
                request.__class__.role_data = RoleSerializer(roles, many=True, active=role).data
        if not role:
            request = clear_roles(request)

        response = self.get_response(request)
        return response
