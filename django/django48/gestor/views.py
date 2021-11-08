# django
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# python
import datetime
import pdb
# gestor
from gestor.models import Articulos,Clientes

from gestor.forms import UserRegisterForm

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

def articuloAdd(request):
    nombre = request.POST['nombre']
    if len(nombre)>=20:
        messages.success(request, "El nombre es demasiado largo")
    else:
        messages.error(request, f"La longitus es de {len(nombre)}")
        # art = Articulos.objects.create(nombre=nombre,seccion=request.POST['seccion'],precio=request.POST['precio'])
    return HttpResponseRedirect('/gestor/articulos')

def valid(nombre,direccion,email,telefono,password,passwordRep):
    errorDict = {}

    # Nombre
    if len(nombre)>30 or len(nombre)<3:
        errorDict['enombre']='El nombre es demasiado corto'
    # direccion
    
    # email
    if len(email)==0:
        errorDict['eemail']='Debe ingresar un correo'

    emailBase = Clientes.objects.filter(email=email)
    if not len(emailBase)==0:
        errorDict['eemail']='Correo electronico no esta disponible'
    
    # telefono
    if not(len(telefono)==10):
        errorDict['etelefono']='Debe tener 10 digitos'
    for i in telefono:
        if ord(i) < 48 or ord(i) > 58:
            errorDict['etelefono']='El telefono no puede contener letras ni caracateres'
            break
    
    # password
    if len(password)>20 or len(password)<8:
        errorDict['epassword']='La contraseña debe ser mayor a 8 y menor a 20 caracteres'
    # passwordRep
    if len(passwordRep)>20 or len(passwordRep)<8:
        errorDict['epasswordRep']='La contraseña debe ser mayor a 8 y menor a 20 caracteres'
    if not password==passwordRep:
        errorDict['epasswordRep']='Las contraseñas no coinciden'

    return errorDict

def clientes(request):
    clientes = Clientes.objects.all()
    fechaActual = datetime.datetime.now()
    diccionario = {
        'fecha':fechaActual,
        'model':'clientes',
        'theme':'Quartz',
        # 'theme':'Sketchy',
        'clientes':clientes.values()
    }
    return render(request,'Users/Clientes/clientes.html',diccionario)

def clientesAdd(req):
    nombre=req.POST['nombre']
    direccion=req.POST['direccion']
    email=req.POST['email']
    telefono=req.POST['telefono']
    password=req.POST['password']
    passwordRep=req.POST['passwordRep']

    status=valid(nombre,direccion,email,telefono,password,passwordRep)
    cliente = {'nombre':nombre,'direccion':direccion,'email':email,'telefono':telefono,'password':password}

    diccionario = {'status':status,'cliente':cliente}
    # pdb.set_trace()
    if len(status)>0:
        messages.error(req, 'Error en formularios de registro')
        return render(req,'Users/Clientes/clientes.html',diccionario)
    else:
        cliente = Clientes.objects.create(nombre=nombre,direccion=direccion,email=email,telefono=telefono,password=password)
        messages.success(req, f'Cliente {nombre} registrado con exito')
        return HttpResponseRedirect('/gestor/clientes')


# Modelo de formularios que usa las clases de django

def userAdd(req):
    if req.method == 'POST':
        # form=UserCreationForm(req.POST)
        form=UserRegisterForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(req,f'El usuario {username} fue creado con exito ')
    else:
        messages.success(req,f'Probando los mensajes')
        form=UserRegisterForm()
        # form=UserCreationForm()
    
    diccionario = {
        'fecha':datetime.datetime.now(),
        'model':'usuarios',
        'header':'Usuarios',
        'formulario':form
    }
    return render(req,'users/users.html',diccionario)