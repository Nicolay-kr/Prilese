from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index_url'),
    path('<str:category>/', views.subcategory, name='category_url'),
    path('<str:category>/<str:slug_subcategory>', views.list_of_products,
         name='subcategory_url'),
    path('<str:category>/<str:slug_subcategory>/<str:slug_product>',
         views.my_product, name='product_url')


] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)