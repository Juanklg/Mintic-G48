from django.contrib import admin
from django.urls import path
from gestor.views import *

urlpatterns = [
    # Articulos
    path('', articulos),
    path('add/', addarticulo),
]
