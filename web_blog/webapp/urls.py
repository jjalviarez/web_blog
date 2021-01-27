from django.urls import path
from web_blog.webapp import views


app_name = "webapp"
urlpatterns = [
        path('', views.home, name='Home'),
        path('tienda/', views.tienda, name='tienda'),
]
