from django.urls import path
from rango import views


rango_patterns = [
    path('', views.index, name='index'),
]