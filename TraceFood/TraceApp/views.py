from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .form import CrearUsuarioForm

# Create your views here.

def home(request):
   return render(request, 'home.html')

def buscar_producto(request):
   productos = Producto.objects.all()
   print(productos)
   
   #buscado =request.GET.get('search')
   #if buscado:
    #  productoBuscado = Producto.objects.filter(title__icontains=buscado)
  
   #return render(request, 'buscar_producto.html', {'productos':productos, 'buscado': buscado, 'productoBuscado': productoBuscado})
   return render(request, 'buscar_producto.html', {'productos':productos})

   
   

   

def escanear_producto(request):
   return render(request, "escanear_producto.html")

def registro(request):
  
   form = UserCreationForm(request.POST)
   
   if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           
           
   context = {'form': form}     
   return render(request, 'registro.html', context)

