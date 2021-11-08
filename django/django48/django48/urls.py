from django.contrib import admin
from django.urls import path,include
from django48.views import *

urlpatterns = [
    # learn django
    path('',saludar),
    path('learn/fonts/',fonts),
    path('learn/tareas/',tareas),
    path('learn/videos/',videos),
    path('learn/calculo/<int:fechaNacimiento>/<int:fechaFutura>',calculo),
    # login
    path('logout/', userLogout),#peticion mixta de usuarios
    path('login/', userLogin),#peticion mixta de usuarios
    # Gestor - Articulo,Pedido,Cliente,Tareas
    path('gestor/', include(('gestor.urls', 'gestor'), namespace='gestor')),
    # Django
    path('admin/', admin.site.urls),
]
