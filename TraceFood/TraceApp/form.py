from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import  User

from .models import *

#class OrderForm(ModelForm):
#   class Meta:
#      model = Order
#      fields = '__all__'
      
class CrearUsuarioForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['nit','nombre', 'correo', 'numero_contacto', 'direccion', 'pais', 'departameno',  'municipio', 'certificaciones', 'rol']