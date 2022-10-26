from djongo import models
import datetime

# Create your models here.

class Proveedor(models.Model):
    nit = models.PositiveBigIntegerField()
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    numero_contacto = models.PositiveBigIntegerField()
    direccion = models.CharField(max_length=200)
    municipio = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    certificaciones = models.CharField(max_length=250)
    rol = models.CharField(max_length=25)
    usuario = models.CharField(max_length=20, default="a")
    contrasena = models.CharField(max_length=15, default="12345")
    
class Res(models.Model):
    id_granja = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
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
    id_receptor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_res = models.ForeignKey(Res, on_delete=models.CASCADE, default=0)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField(default=datetime.date.today)
    direccion_recepcion = models.CharField(max_length=200)
    temperatura = models.FloatField()
    estado = models.CharField(max_length=50)
    comentarios = models.CharField(max_length=300)

class Reporte(models.Model):
    id_producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.IntegerField(default=3)
    fecha_reporte = models.DateField(default=datetime.date.today)
    comentarios = models.CharField(max_length=300)