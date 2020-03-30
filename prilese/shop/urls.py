from django.urls import path
from django.views.generic import View
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import CreateOrder,Index

app_name = 'shop'
urlpatterns = [
    path('', Index.as_view(), name='index_url'),
    path('contact/', views.contact, name='contact_url'),
    path('delivery/', views.delivery, name='delivery_url'),
    path('search/', views.search, name='search_url'),
    path('order/', CreateOrder.as_view(), name='order_url'),
    path('cart/', views.view_cart, name='cart_url'),
    path('cart/create/<str:slug_product>', views.add_product_to_cart,
         name='cart_add_url'),
    path('cart/delete/<str:slug_product>', views.delete_product_from_cart,
         name='cart_delete_url'),
    path('<str:category>/', views.subcategory, name='category_url'),
    path('<str:category>/<str:slug_subcategory>', views.list_of_products,
         name='subcategory_url'),
    path('<str:category>/<str:slug_subcategory>/<str:slug_product>',
         views.my_product, name='product_url'),

]
