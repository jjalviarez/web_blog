
from django.shortcuts import render, HttpResponse
from .models import Category, Post
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.filter(post__in = posts).distinct()


    return render(request,'blog/blog.html',{'posts': posts, 'categories':categories})

def category(request,category_id):
    posts = Post.objects.filter(category__id__exact=category_id)
    categories = Category.objects.filter(post__in = posts).distinct()

    return render(request,'blog/blog.html',{'posts': posts, 'categories': categories})


