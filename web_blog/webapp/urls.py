from django.urls import path
from web_blog.webapp import views


app_name = "webapp"
urlpatterns = [
        path('', views.home, name='Home'),
        path('tienda/', views.tienda, name='tienda'),
        path('blog/', views.blog, name='blog'),
        path('contacto/', views.contacto, name='contacto'),
]
