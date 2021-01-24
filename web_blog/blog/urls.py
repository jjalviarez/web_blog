from django.urls import path
from web_blog.blog import views


app_name = "blog"
urlpatterns = [
        path('', views.blog, name='blog'),
]
