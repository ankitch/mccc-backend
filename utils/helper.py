from django.shortcuts import get_object_or_404

from apps.users.models import Role
from apps.users.serializers import UserSerializer, RoleSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    company = get_object_or_404(Role.objects.filter(user=user.id))
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data,
        'role': RoleSerializer(instance=company, many=False).data
    }
