from django.shortcuts import render
from django.shortcuts import render, redirect,HttpResponseRedirect

from TraceApp.models import Producto

# Create your views here.

def home(request):
   return render(request, 'home.html')

def buscar_producto(request):
   searchTerm =request.GET.get('productoBuscado')
   if searchTerm:
      movies = Producto.objects.filter(id_producto__icontains=searchTerm)
   #else:
      #movies = Movie.objects.all()
   return render(request, 'buscar_producto.html', {'searchTerm':searchTerm, 'productos': Producto})

   

def escanear_producto(request):
   return render(request, "escanear_producto.html")

