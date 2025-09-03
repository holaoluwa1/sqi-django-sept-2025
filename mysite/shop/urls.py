from django.urls import path 
from . import views 




urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('cart/', views.shop_cart, name='shop_cart'),


]