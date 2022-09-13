from pyexpat import model
from django.db import models

# ¿COMO HACER LAS RELACIONES; EN ESPECIAL LAS FORANEAS

#https://qastack.mx/programming/6928692/how-to-express-a-one-to-many-relationship-in-django
# ¿DEBO HACER UNA APP PARA LAS COSAS RELACIONADAS CON LA VACA Y OTRA PARA LAS RELACIONADAS CON LOS USUARIOS?
# ID_AUTOINCREMENTABLE
class Proveedor(models.Model):
   proveedor_ID = models.AutoField(primary_key=True, auto_created = True)
   proveedor_NIT = models.AutoField(primary_key=False)
   nombre = models.CharField(max_length=50)
   correo = models.EmailField( max_length= 50)
   telefono_contacto = models.CharField(max_length=10)
   direccion =models.CharField(max_length=50)
   municipio = models.CharField(max_length=50)
   departamento = models.CharField(max_length=50)
   pais = models.CharField(max_length=50)
   certificaciones = models.BooleanField()
   rol_deparmento = models.CharField(max_length=50)
   


class Recepcion(models.Model):
   recepcion_ID = models.AutoField(primary_key=True)
   #¿Puedo hacer un ID compuesto?
   fecha = models.DateField()
   hora = models.TimeField( auto_now=False, auto_now_add=True)
   id_receptor = models.CharField(max_length=50)
   id_producto = models.CharField(max_length=10)
   #Como solucionar la relacion con el producto y las reces
   
   temperatura =models.CharField(max_length=50)
   estado = models.CharField(max_length=50)
   comentarios = models.CharField(max_length=200)
   

class Producto(models.Model):
   producto_ID = models.AutoField(primary_key=True)
   res_ID = models.AutoField()
   codigo_qr = models.ImageField(upload_to=None)
   # ¿IMAG -> Si lo voy a almacenar E O URL ->Si se trabaja externo???
   #UPLOAD?????
   corte = models.CharField(max_length=50)
   estado = models.CharField(max_length=50)
   peso_Kg = models.IntegerField()
   
class Res(models.Model):
   res_ID = models.AutoField()
   id_granja = models.CharField(max_length=50)
   fecha_nacimiento = models.DateField()
   fecha_muerte = models.DateField()
   estado = models.CharField(max_length=50)
   peso_Kg = models.IntegerField()
   
class Reportes(models.Model):
   reporte_ID = models.AutoField()
   reporte_ID = models.AutoField()
   fecha= models.DateField(auto_now=True)
   comectario = models.CharField(max_length=50)
   

      
