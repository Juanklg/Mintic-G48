from django.contrib import admin
from django.urls import path
from gestor.views import *

urlpatterns = [
    # Articulos
    path('articulos/', articulos),
    path('articuloAdd/', articuloAdd),
    # Clientes
    path('clientes/', clientes),#peticion get clientes
    path('clienteAdd/', clientesAdd),#peticion post clientes
    # Users
    path('usuarioAdd/', userAdd),#peticion mixta de usuarios
]



