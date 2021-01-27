from django.urls import path
from web_blog.contact import views


app_name = "contact"
urlpatterns = [
        path('', views.contact, name='contact'),
]
