from django.http import HttpResponse
from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    # request is the HTTP request that the user made in order to acces our web server
    return render(request, "hello/index.html")

def mayur(request):
    return HttpResponse("Hello, Indian!")


def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()

    })



