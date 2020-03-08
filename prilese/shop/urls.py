from django.urls import path

from . import views

app_name = 'Shop'
urlpatterns = [
    path('', views.index, name='index'),
]