from django.urls import path
from web_blog.servicios import views


app_name = "servicios"
urlpatterns = [
        path('', views.servicios, name='servicios'),
]
