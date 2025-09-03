from django.urls import path
from . import views


urlpatterns = [
    path('',views.commmunity, name='community'),

]