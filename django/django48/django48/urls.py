from django.contrib import admin
from django.urls import path,include
from django48.views import *

urlpatterns = [
    path('',saludar),
    path('fonts/',fonts),
    path('tareas/',tareas),
    path('calculo/<int:fechaNacimiento>/<int:fechaFutura>',calculo),
    path('admin/', admin.site.urls),
    # Articulos
    path('art/', include(('gestor.urls', 'gestor'), namespace='gestor')),
]
