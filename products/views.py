from django.shortcuts import render
from products.models import ProductModel

def home_page(request):
    products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, template_name='index.html', context=context)

def products_page(request):
    products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, template_name='products.html', context=context)
