from django.urls import path
from . import views

app_name='myapp_yuzuri'

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('like', views.like, name='like'),
    path('dislike', views.dislike, name='dislike'),
    path('birthday', views.birthday, name='birthday'),
]
