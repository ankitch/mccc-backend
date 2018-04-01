import xlwt
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from apps.tanks.models import Customer, List

class UploadFileForm(forms.Form):
    file = forms.FileField()

def export_customers(request, pk):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('customers')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'full_name', 'email', 'phone', 'add_fields'] # add_fields
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
            new_customers = []
            data = request.FILES['file']
            map_dict = ['full_name', 'email', 'phone', 'add_fields']
            create_customers = []

            for cus in data:
                kgs = {}
                for index, val in enumerate(cus):
                    import ipdb
                    ipdb.set_trace()

                    attr = map_dict[index]
                    if attr in ['email', 'phone']:
                        val = val
                    kgs[attr] = val
                customer = Customer(**kgs)
                customer.id = None
                new_customers.append(customer)

