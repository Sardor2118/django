from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .models import ProductModel, CategoryModel, CartModel
from .handler import bot


def home_page(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, template_name='index.html', context=context)


def products_page(request):
    products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, template_name='products.html', context=context)


# login
class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_page')


def logout_view(request):
    logout(request)
    return redirect('home_page')


def single_product(request, pk):
    product = ProductModel.objects.get(pk=pk)  # 2
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
        checker = ProductModel.objects.get(pk=pk)  # 2

        if checker.product_amount >= int(request.POST.get('pr_count')):
            CartModel.objects.create(user_id=request.user.id, user_product=checker,
                                     user_product_quantity=int(request.POST.get('pr_count'))).save()
            return redirect('/user_cart')
        else:
            return redirect(f'product/{checker.pk}')


def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)  # 4
    if request.method == 'POST':
        main_text = 'Новый заказ: \n'

        for i in cart:
            main_text += (f'📦 Товар: {i.user_product}\n'
                         f'🌐 Кол-во: {i.user_product_quantity}\n'
                         f'👤 Пользователь: {i.user_id}\n'
                         f'💸 Цена: {i.user_product.product_price}\n')
            bot.send_message(-1001804805193, main_text)
            cart.delete()
            return redirect('/')
    else:
        context = {'cart': cart}
        return render(request, template_name='cart.html', context=context)
def delete_user_cart(request, pk):
    product_delete = ProductModel.objects.get(pk=pk)

    CartModel.objects.filter(user_id=request.user.id, user_product=product_delete).delete()

    return redirect('/user_cart')


def total_price(request):
    user_products = ProductModel.objects.all()  # Query your UserProduct model
    total_price = sum(product.price for product in user_products)  # Calculate total price
    context = {'total_price': total_price}
    return render(request, 'cart.html', context)