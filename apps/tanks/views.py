import ast

import xlwt
from django import forms
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from haystack.management.commands import rebuild_index, update_index

from apps.tanks.models import Customer, List


class UploadFileForm(forms.Form):
    file = forms.FileField()


def export_customers(request, pk):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('customers')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'full_name', 'email', 'phone', 'add_fields']  # add_fields
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    list = get_object_or_404(List, pk=pk)
    rows = Customer.objects.filter(lists=pk).values_list('id', 'full_name', 'email', 'phone', 'add_fields')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s_customers.xls"' % list.name.lower().replace(' ', '_')
    wb.save(response)
    return response


def import_customers(request, pk):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file_handle = request.FILES['file'].get_array()[1:]
            map_dict = ['full_name', 'email', 'phone', 'add_fields']
            new_customers = []
            customer_ids = []
            for item in file_handle:
                dict_cus = {}
                for index, val in enumerate(item):
                    attr = map_dict[index]

                    if index == 3:
                        dict_cus[attr] = val = ast.literal_eval(val)
                    else:
                        dict_cus[attr] = val
                dict_cus['company_id'] = request.company.id
                # import ipdb
                # ipdb.set_trace()
                customer = Customer(**dict_cus)
                customer.id = None
                new_customers.append(customer)
            try:
                res = Customer.objects.bulk_create(new_customers)
                for cus in res:
                    customer_ids.append(cus.id)
            except IntegrityError:
                return HttpResponseBadRequest('ERROR')
            lists = get_object_or_404(List, pk=pk)
            lists.customers.add(*customer_ids)
            update_index.Command().handle(interactive=False)

            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
