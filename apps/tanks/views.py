from django.shortcuts import render, get_object_or_404

# Create your views here.

# def tanks_api():
from pyexcel import get_sheet
from rest_framework.response import Response
import django_excel as excel
from apps.tanks.models import Customer, List


def export_customers(request, pk):
    list = get_object_or_404(List, pk=pk)
    query = Customer.objects.filter(lists=pk).distinct()
    columns = ['id', 'full_name', 'email', 'phone']
    sheet = get_sheet(query_sets=query, column_names=columns)
    response = excel.make_response(sheet, 'xls', file_name='sheet_name')
    response['Content-Disposition'] = 'attachment; filename="%s_customers.xls"' % list.name.lower().replace(' ', '_')
    return response

