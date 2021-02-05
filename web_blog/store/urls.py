from django.urls import path
from web_blog.store import views


app_name = "store"
urlpatterns = [
        path('', views.store, name='store'),
]
