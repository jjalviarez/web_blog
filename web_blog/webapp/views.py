
from django.shortcuts import render, HttpResponse
from web_blog.servicios.models import Servicio


# Create your views here.

def home(request):

    return render(request,'pages/home.html')


def servicios(request):
    servicios = Servicio.objects.all()

    return render(request,'webapp/servicios.html',{'servicios': servicios})



def tienda(request):

    return render(request,'webapp/tienda.html')


def blog(request):

    return render(request,'webapp/blog.html')


def contacto(request):

    return render(request,'webapp/contacto.html')




