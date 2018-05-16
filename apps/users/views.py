from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.models import User


@api_view(['POST'])
def get_fcm_reg_id(request, *args, **kwargs):
    user = request.user.id
    reg_id = request.data['reg_id']
    try:
        User.objects.filter(pk=user).update(fcm_reg_id=reg_id)
    except IndexError:
        pass
    return Response({'status': 'added'})
