from django.shortcuts import render, HttpResponse

from django.contrib import admin
from django.urls import path 
from contact import views

# Create your views here.


def phone_us(request):
    return HttpResponse("phone us: '+2348167866468'")




def email_us(request):
    return HttpResponse("email us: 'holaoluwa@gmail.com'")
