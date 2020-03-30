from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from .forms import OrderForm
from django.views.generic import View


# from django.http import HttpResponse

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'shop/index.html')


# def index(request):
#     return render(request, 'shop/index.html')


def subcategory(request, category):
    list_of_subcategory = models.Subcategory.objects.filter(category=category)

    return render(request, 'shop/subcategory.html',
                  context={"subcategories": list_of_subcategory})


def list_of_products(request, slug_subcategory, category):
    subcategory = models.Subcategory.objects.get(
        slug_subcategory=slug_subcategory)
    products = models.Product.objects.filter(subcategory=subcategory)

    return render(request, 'shop/list.html', context=locals())


def my_product(request, slug_subcategory, slug_product, category):
    product = models.Product.objects.get(slug_product=slug_product)
    return render(request, 'shop/product.html', context=locals())


# def basket(request, slug_product):
# product = models.Product.objects.get(slug_product=slug_product)
# return render(request, 'shop/basket.html', context=locals())


def view_cart(request):
    cart = models.Cart.objects.all()
    total_price = 0
    for i in cart:
        total_price += i.product.price * float(i.quantity)

    return render(request, 'shop/cart.html', context=locals())


def add_product_to_cart(request, slug_product):
    product = models.Product.objects.get(slug_product=slug_product)
    try:
        cart = models.Cart.objects.get(product=product)
    except:
        models.Cart.objects.create(product=product)
    return redirect('shop:cart_url')


def delete_product_from_cart(request, slug_product):
    product = models.Product.objects.get(slug_product=slug_product)
    product_in_cart = models.Cart.objects.get(product=product)
    product_in_cart.delete()
    return redirect('shop:cart_url')


class CreateOrder(View):

    def get(self, request):
        form = OrderForm()
        return render(request, 'shop/create_order.html', context={'form': form})

    def post(self, request):
        bound_form = OrderForm(request.POST)

        if bound_form.is_valid():
            new_order = bound_form.save()
            # product_in_cart= models.Cart.objects.all()
            # product_in_cart.delete()

            return redirect('shop:index_url')

        return render(request, 'shop/create_order.html',
                      context={'form': bound_form})


def search(request):
    query = request.GET.get('q')
    products = models.Product.objects.filter(title__icontains=query)
    return render(request, 'shop/search.html', context={'products': products})


def contact(request):
    return render(request, 'shop/contact.html')


def delivery(request):
    return render(request, 'shop/delivery.html')
