from django.http import HttpResponse,HttpResponseRedirect
from gestor.models import Articulos
from django.shortcuts import render

from django.contrib import messages

def articulos(request):    
    articulos = []
    if len(request.GET)>=1:
        search = request.GET['search']
        articulos = Articulos.objects.filter(nombre__icontains=search) | Articulos.objects.filter(seccion__icontains=search)
    else:
        articulos = Articulos.objects.all()
    secciones = set()
    for art in articulos.values():
        secciones.add(art['seccion'])    
    diccionario = {
        'articulos':articulos.values(),
        'model':'articulos',
        'secciones':secciones
    }
    return render(request,'articulos/articulos.html',diccionario)

def addarticulo(request):
    nombre = request.POST['nombre']
    if len(nombre)>=20:
        messages.success(request, "El nombre es demasiado largo")
    else:
        messages.error(request, f"La longitus es de {len(nombre)}")
        # art = Articulos.objects.create(nombre=nombre,seccion=request.POST['seccion'],precio=request.POST['precio'])
    return HttpResponseRedirect('/art/articulos')
