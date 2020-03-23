from django.shortcuts import render
from . import models

# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def subcategory(request, category):
    list_of_subcategory = models.Subcategory.objects.filter(category=category)

    return render(request, 'shop/subcategory.html', context={"goods": list_of_subcategory})

def list_of_products(request,slug,category):
    subcategory = models.Subcategory.objects.get(slug=slug)
    products = models.Product.objects.filter(subcategory=subcategory)

    return render(request, 'shop/list.html', context=locals())
