from django.urls import path 

from . import views


urlpatterns = [
    path('libary/', views.dashboard, name="libary"),
]


