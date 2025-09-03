from django.shortcuts import render, HttpResponse

# Create your views here.



def shop_home(request):
    return HttpResponse("welcome to shop")



def shop_cart(request):
    return HttpResponse("your shopping cart")
