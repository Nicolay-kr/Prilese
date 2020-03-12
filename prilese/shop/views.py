from django.shortcuts import render
from . import models

# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def category_of_kinds(request, category):
    list_of_kinds = models.Product.objects.filter(category=category)

    return render(request, 'shop/category.html', context={"goods": list_of_kinds})

def kind_of_good(request,kind,category):
    list_of_goods = models.Product.objects.filter(kind=kind)
    return render(request, 'shop/list.html', context={"goods": list_of_goods})
