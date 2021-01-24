
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request,'pages/home.html')

def tienda(request):

    return render(request,'webapp/tienda.html')


def blog(request):

    return render(request,'webapp/blog.html')


def contacto(request):

    return render(request,'webapp/contacto.html')




