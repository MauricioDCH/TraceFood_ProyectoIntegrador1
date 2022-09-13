from multiprocessing.forkserver import read_signed
from winreg import QueryReflectionKey
from django.db import models

# Create your models here.




'''
class PRODUCTO(models.Model):
   producto_id = models.CharField(primary_key= True, max_length=20)
   res_id = models.CharField(max_length=20)
   corte = models.CharField(max_length=20)
   estado = models.CharField(max_length=20)
   peso_g = models.FloatField()
   QR = models.ImageField(upload_to=None, NULL = True)
   
class RES(models.Model):
   res_ID = models.AutoField(primary_key= True)
   fecha_nacimiento = models.CharField(max_length=20)
   fecha_muerte = models.CharField(max_length=20)
   estado = models.CharField(max_length=20)
   peso_Kg = models.FloatField()

class PROVEEDOR(models.Model):
   proveedor_ID = models.AutoField(primary_key=True)
   nombre = models.CharField(max_length=20)
   apellido = models.CharField(max_length=20)
   correo = models.EmailField( max_length= 50)
   telefono = models.CharField(max_length=10)
   direccion =models.CharField(max_length=20)
   municipio = models.CharField(max_length=20)
   departamento = models.CharField(max_length=20)
   pais = models.CharField(max_length=20)
   certificaciones = models.BooleanField()
   rol = models.CharField(max_length=20)
   '''