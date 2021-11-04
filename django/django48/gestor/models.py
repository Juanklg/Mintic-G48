from django.db import models
from django.db.models.base import Model

class Clientes(models.Model):
    nombre=models.CharField(max_length=30,blank=False,default="nulo")
    direccion=models.CharField(max_length=50,blank=False,default="nulo")
    email=models.EmailField(max_length=50,unique=True,blank=False,default="nulo")    
    telefono=models.CharField(max_length=15,blank=False,default="nulo")
    password=models.CharField(max_length=15,blank=False,default="nulo")
    def __str__(self):
        return f"Nombre_del_Cliente: {self.nombre} - Email_del_cliente: {self.email}"

class Articulos(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    def __str__(self):
        return "%s - Seccion: %s - Precio: %s" %(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class Tareas(models.Model):
    proyecto=models.CharField(max_length=15)
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    estado=models.IntegerField(default=0)
    responsable=models.CharField(max_length=30)