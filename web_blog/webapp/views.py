
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request,'pages/home.html')

def tienda(request):

    return render(request,'webapp/tienda.html')








