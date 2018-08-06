from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.send.models import Replies
from apps.send.schedules import schedule_sms
from apps.send.serializers import RepliesSerializer
from apps.send.utils import send_sms_fcm, send_misscall_info, sync_data_message
from apps.tanks.models import Campaign
from apps.users.models import User


class SendSMS(APIView):
    def post(self, request, format=None):
        campaign = request.data['campaign']
        segment = request.data['segment']
        reg_id = User.objects.get(pk=request.user.id).fcm_reg_id
        send = send_sms_fcm(campaign, segment, reg_id)
        return Response(send)


class ScheduleCampaign(APIView):
    def post(self, request, format=None):
        next_run = request.data.get('next_run')
        schedule_type = request.data.get('sch_type')
        repeats = request.data.get('repeat')
        minutes = request.data.get('minutes')
        channel = request.data.get('channels')

        campaigns = request.data.get('campaign')
        segments = request.data.get('segment')

        fcm_registration_id = User.objects.get(pk=request.user.id).fcm_reg_id

        sms_func = 'apps.send.utils.send_sms_fcm'

        if channel == "SMS":
            sch = schedule_sms(sms_func, campaigns, segments, fcm_registration_id, next_run, schedule_type, repeats,
                               minutes)

        return Response({'schedule': 'created'})


class PushDataMessage(APIView):
    def post(self, request, format=None):
        id = request.data['campaign']
        campaign = Campaign.objects.get(pk=id)
        fcm_reg_id = request.user.fcm_reg_id
        send = send_misscall_info(campaign, fcm_reg_id)
        print(send)
        return Response(send)


class SyncDataMessage(APIView):
    def get(self, request, format=None):
        fcm_reg_id = request.user.fcm_reg_id
        sync = sync_data_message(fcm_reg_id)
        print(sync)
        return Response(sync)


class CreateListMixin:
    """Allows bulk creation of a resource."""

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)


class RepliesViewset(CreateListMixin, viewsets.ModelViewSet):
    serializer_class = RepliesSerializer

    def get_queryset(self):
        company = self.request.company
        return Replies.objects.filter(company_id=company)


class SendMessage(APIView):
    def post(self, request, format=None):
        to_number = request.data['to_number']
        message = request.data['message']


        import ipdb
        ipdb.set_trace()
