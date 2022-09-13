from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
   return render(request, 'pages/home.html')

def nosotros(request):
   return render(request, 'pages/nosotros.html')

def productoBuscar(request):
   return render (request, 'producto/index.html' )

def productoAgregar(request):
   return render(request, 'producto/crear.html')

def productoEditar(request):
   return render(request, 'producto/editar.html')

def usuario(request):
   return render(request, 'usuario/index.html')
