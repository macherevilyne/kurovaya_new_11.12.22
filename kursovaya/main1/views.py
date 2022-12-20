from django.shortcuts import render, redirect

from .models import *
from django.core.paginator import Paginator
from .forms import CarrierForm




def actual(request):  # функция запроса
    cargo = Actual.objects.all().order_by(
        'date_of_transportation')  # получение кверисет всех обьектов, полей из созданных записей
    paginator = Paginator(cargo, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        "cargo": page,  # запись их в контексный словарь
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'actual.html', context)  # возвращение слова и вывод в шаблон


def carrier(request):
    carrier_ = Carrier.objects.all().order_by('date')
    paginator = Paginator(carrier_, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    if request.method == 'POST':
        form = CarrierForm(request.POST)
        if form.is_valid():

            carrier = form.save(commit=False)
            carrier.user = request.user
            carrier.save()
            return redirect('carrier')

    else:
        form = CarrierForm()

    context = {'form': form,
               'carrier_': page,
               'is_paginated': is_paginated,
               'next_url': next_url,
               'prev_url': prev_url,
               }
    return render(request, 'carrier.html', context)



# Удаление созданных обьектов

def deletecarrier(request, carrier_id):
    item = Carrier.objects.get(pk=carrier_id)

    if request.user == item.user:
        Carrier.objects.filter(id=carrier_id).delete()
        return redirect('carrier')
    else:
        return redirect('carrier')



