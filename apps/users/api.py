from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.users.models import Role, Company
from apps.users.serializers import RoleSerializer, CompanySerializer


class RoleViewSet(viewsets.GenericViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    @list_route(methods=['POST'])
    def switch(self, request):
        try:
            role = Role.objects.get(id=request.data.get('id'), user=request.user)
            request.session['role'] = role.id
            return Response(RoleSerializer(role).data)
        except Role.DoesNotExist:
            raise ValidationError('Invalid role')


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        company = self.request.company
        return Company.objects.filter(id=company.id)
