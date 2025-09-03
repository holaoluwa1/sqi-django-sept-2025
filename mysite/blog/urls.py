from django.urls import path
from . import views



urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/', views.blog_post, name='blog_post'),
    path('about/',views.blog_about, name='blog_about'),
]