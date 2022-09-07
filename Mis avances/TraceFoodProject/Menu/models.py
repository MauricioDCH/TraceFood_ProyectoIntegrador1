from pyexpat import model
from django.db import models

# Modelo para almacenar información del usuario.

class Users(models.Model):
   userID = models.AutoField(primary_key=True)
   userDeparment= model.models.CharField(max_length=50)
   

# Modelo para almacenar impormación del producto (vaca).
class Product(models.Model):
   productoID = models.AutoField(primary_key=True)
   corte = model.models.CharField(max_length=50)
   procedencia = model.models.CharField(max_length=50)
   fecha_llegada = model.models.DateField()
   tempreratura_promedio = model.models.CharField(max_length=50)
   
      
