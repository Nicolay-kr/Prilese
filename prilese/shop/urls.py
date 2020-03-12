from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index_url'),
    path('<str:category>/', views.category_of_kinds, name='category_url'),
    path('<str:category>/<str:kind>', views.kind_of_good, name='kind_url'),


]