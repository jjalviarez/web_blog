from django.urls import path
from web_blog.webapp import views


urlpatterns = [
        path('', views.home, name='Home'),
        path('servicios', views.servicios, name='Servicios'),
        path('tienda', views.tienda, name='Tienda'),
        path('blog', views.blog, name='Blog'),
]
