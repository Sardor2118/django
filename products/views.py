from django.shortcuts import render, redirect
from products.models import ProductModel, CategoryModel
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout

def home_page(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, template_name='index.html', context=context)

def products_page(request):
    products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, template_name='products.html', context=context)

# login code
class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_page')

def logout_view(request):
    logout(request)
    return redirect('home_page')

def single_product(request, pk):
    product = ProductModel.objects.get(pk=pk)
    context = {'product': product}
    return render(request, template_name='single-product.html', context=context)

def search_products(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')

        try:
            exact_product = ProductModel.objects.get(product_title__icontains=get_product)

            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')

def add_products_to_user_cart(request, pk):
    if request.method == 'POST':
        checker = ProductModel.objects.get(pk=pk)

        if checker.product_amount >= int(request.POST.get('pr.count')):
            pass