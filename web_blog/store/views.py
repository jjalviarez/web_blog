from django.shortcuts import render, HttpResponse
from .models import Category, Product


# Create your views here.
def store(request):
    products = Product.objects.all()
    categories = Category.objects.filter(product__in = products).distinct()


    return render(request,'store/store.html',{'products': products, 'categories':categories})

def category(request,category_id):
    products = Product.objects.filter(category__id__exact=category_id)
    categories = Category.objects.filter(product__in = products).distinct()

    return render(request,'store/store.html',{'product': products, 'categories': categories})
