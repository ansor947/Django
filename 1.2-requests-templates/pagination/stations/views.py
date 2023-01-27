from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import os
from pagination.settings import BASE_DIR


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    BUS_STATION_CSV = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')
    page_number = int(request.GET.get("page", 1))
    bus_stations_list = Paginator(BUS_STATION_CSV, 10)
    page = bus_stations_list.get_page(page_number)

    context = {
        'bus_stations': bus_stations_list,
        'page': page,
              }
    return render(request, 'index.html', context)
