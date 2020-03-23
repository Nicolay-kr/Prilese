from django.shortcuts import render
from . import models


# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def subcategory(request, category):
    list_of_subcategory = models.Subcategory.objects.filter(category=category)

    return render(request, 'shop/subcategory.html',
                  context={"products": list_of_subcategory})


def list_of_products(request, slug_subcategory, category):
    subcategory = models.Subcategory.objects.get(
        slug_subcategory=slug_subcategory)
    products = models.Product.objects.filter(subcategory=subcategory)

    return render(request, 'shop/list.html', context=locals())


def my_product(request, slug_subcategory, slug_product, category):
    product = models.Product.objects.get(slug_product=slug_product)
    return render(request, 'shop/product.html', context=locals())
