from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from ProductApp.models import ProductModle
from ProductApp.forms import ProductSearchForm

# Create your views here.

def home_view(request):
    products = ProductModle.objects.all()
    form = ProductSearchForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get('category')
        brand = form.cleaned_data.get('brand')
        warranty = form.cleaned_data.get('warranty')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if category:
            products = ProductModle.objects.filter(category=category)
        if brand:
            products = ProductModle.objects.filter(brand=brand)
        if warranty:
            products = ProductModle.objects.filter(warranty=warranty)
        if category and brand:
            products = ProductModle.objects.filter(category=category, brand=brand)
        if category and warranty:
            products = ProductModle.objects.filter(category=category, warranty=warranty)
        if brand and warranty:
            products = ProductModle.objects.filter(brand=brand, warranty=warranty)
        if category and brand and warranty:
            products = ProductModle.objects.filter(category=category, brand=brand, warranty=warranty)
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)

        context = {
            'products': products,
            'form': form,
            'title': 'HOME',
        }

        return render(request, 'ProductApp/home.html', context=context)    

    else:
        products = ProductModle.objects.all() 


    context = {
        'products': products,
        'title': 'HOME',
    }

    return render(request, 'ProductApp/home.html', context=context)

def search_view(request):
    products = ProductModle.objects.all()
    form = ProductSearchForm(request.GET)

    # if form.is_valid():
    #     category = form.cleaned_data.get('category')
    #     brand = form.cleaned_data.get('brand')
    #     warranty = form.cleaned_data.get('warranty')
    #     min_price = form.cleaned_data.get('min_price')
    #     max_price = form.cleaned_data.get('max_price')

    #     if category:
    #         products = ProductModle.objects.filter(category=category)
    #     if brand:
    #         products = ProductModle.objects.filter(brand=brand)
    #     if warranty:
    #         products = ProductModle.objects.filter(warranty=warranty)
    #     if category and brand:
    #         products = ProductModle.objects.filter(category=category, brand=brand)
    #     if category and warranty:
    #         products = ProductModle.objects.filter(category=category, warranty=warranty)
    #     if brand and warranty:
    #         products = ProductModle.objects.filter(brand=brand, warranty=warranty)
    #     if category and brand and warranty:
    #         products = ProductModle.objects.filter(category=category, brand=brand, warranty=warranty)
    #     if min_price is not None:
    #         products = products.filter(price__gte=min_price)
    #     if max_price is not None:
    #         products = products.filter(price__lte=max_price)  

    # else:
    #     products = ProductModle.objects.all() 

    products_data = list(products.values())

    context = {
        'products': products_data,
    }

    return JsonResponse(context, safe=False)