from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from ProductApp.models import ProductModle
from ProductApp.forms import ProductSearchForm

# Create your views here.

def home_view(request):
    products = ProductModle.objects.all() 
    form = ProductSearchForm(request.GET)

    context = {
        'products': products,
        'title': 'HOME',
        'form': form,
    }

    return render(request, 'ProductApp/home.html', context=context)

def search_view(request):
    products = ProductModle.objects.all()    
    products_data = list(products.values())

    context = {
        'products': products_data,
    }

    return JsonResponse(context, safe=False)