from django.shortcuts import render, HttpResponse

# Create your views here.


def blog_home(request):
    return HttpResponse("welcome")


def blog_post(request):
    return HttpResponse("blog post")


def blog_about(request):
    return HttpResponse("about the blog")
