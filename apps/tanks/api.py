from .serializers import CustomerSerializer
from rest_framework import viewsets
from .models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by( '-id')
    serializer_class = CustomerSerializer
