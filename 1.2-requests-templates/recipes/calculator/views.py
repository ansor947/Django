from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
} 

def counter(request, dishs, quantitys):
    quantity = int(request.GET.get("quantity", 1))
    dish = request.GET.get("quantity", 1)
    context = {
        'recipes_list':DATA,
        'quantity':quantity,
        'dish':dish
              }
    return render(request, 'index.html', context)