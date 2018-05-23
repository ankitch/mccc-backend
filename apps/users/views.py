from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User


class FCMDeviceRegistration(APIView):
    def post(self, request, format=None):

        user = request.user.id
        reg_id = request.data['reg_id']
        try:
            User.objects.filter(pk=user).update(fcm_reg_id=reg_id)
            return Response({'status': 'added'})

        except User.DoesNotExist:
            raise
