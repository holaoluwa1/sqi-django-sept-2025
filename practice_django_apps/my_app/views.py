from django.shortcuts import render, HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("welcome to my app")
