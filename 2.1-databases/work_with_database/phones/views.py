from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_value = request.GET.get("sort")
    template = 'catalog.html'
    phones_all = Phone.objects.all()

    if sort_value == 'min_price':
        phones_objects = phones_objects.order_by('price')
    elif sort_value == 'max_price':
        phones_objects = phones_objects.order_by('price').reverse()
    elif sort_value == 'name':
        phones_objects = phones_objects.order_by('name')
    
    context = {

        'phones' : phones_all

              }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug)
    context = {

        'phone' : phone

              } 
    return render(request, template, context)

