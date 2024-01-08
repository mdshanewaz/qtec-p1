from django.shortcuts import render, HttpResponse
from ProductApp.models import ProductModle

# Create your views here.

def home_view(request):
    products = ProductModle.objects.all()
    context = {
        'products' : products,
        'title': 'HOME',
    }
    return render(request, 'ProductApp/home.html', context=context)
