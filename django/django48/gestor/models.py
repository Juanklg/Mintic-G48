from django.db import models
from django.db.models.base import Model


class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    tfno=models.CharField(max_length=13)

    def __str__(self):
        return f"Nombre_del_Cliente: {self.nombre} - Email_del_cliente: {self.email}"

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return "Nombre: %s - Seccion: %s - Precio: %s" %(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()