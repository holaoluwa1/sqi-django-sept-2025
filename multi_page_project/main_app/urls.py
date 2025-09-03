from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name="welcome"),
    path('about/', views.about, name="about_us"),
    path('contact/', views.contact, name= "contact_us"),


]