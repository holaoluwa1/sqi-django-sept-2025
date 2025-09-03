from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.homepage, name="home"),
    path('profile/', views.profilepage, name="profile"),
    path('service/', views.servicepage, name= "service"),
    path('help/', views.helppage, name="help"),


]