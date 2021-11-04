from django.contrib import admin
from django.urls import path
from gestor.views import *

urlpatterns = [
    # Articulos
    path('articulos/', articulos),
    path('articuloAdd/', articuloAdd),
    # Clientes
    path('clientes/', clientes),
    path('clienteAdd/', clientesAdd),
    # Users
    path('usuarios/', userAdd),
    path('usuariosAdd/', clientesAdd),
]



