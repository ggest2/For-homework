from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='main'),
    path('<str:tag>/',views.restaurant,name='restaurants'),
]