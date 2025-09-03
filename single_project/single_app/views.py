from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def profilepage(request):
    return render(request, "profilepage.html")
    

def servicepage(request):
    return render (request, "servicepage.html") 


def helppage(request):
    return render(request,"helppage.html")
