from email.policy import default
from django.db import models

# Create your models here.

from django.db import models
from django import forms


import datetime

# Create your models here.

class Proveedor(models.Model):
    nit = models.PositiveBigIntegerField()
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    numero_contacto = models.PositiveBigIntegerField()
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    departameno = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    certificaciones = models.CharField(max_length=250)
    rol = models.CharField(max_length=25)
    
class Res(models.Model):
    id_granja = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    fecha_muerte = models.DateField()
    peso = models.FloatField()
    estado = models.TextField()

class Producto(models.Model):
    id_res = models.ForeignKey(Res, on_delete=models.CASCADE)
    parte = models.CharField(max_length=50)
    codigo_qr = models.ImageField() #upload_to='movie/images/'
    estado = models.CharField(max_length=50)
    peso = models.FloatField()

class Ficha_Recepcion(models.Model):
    id_receptor = models.ForeignKey(User, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField(default=datetime.date.today)
    direccion_recepcion = models.CharField(max_length=200)
    temperatura = models.FloatField()
    estado = models.CharField(max_length=50)
    comentarios = models.CharField(max_length=300)

class Reporte(models.Model):
    id_producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=300)
