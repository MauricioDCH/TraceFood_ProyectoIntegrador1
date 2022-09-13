from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('producto/buscar/', views.productoBuscar, name='producto_buscar'),
    path('producto/agregar/', views.productoAgregar, name='producto_agregar'),
    path('producto/editar/', views.productoEditar, name='producto_editar'),
    path('usuario/', views.usuario, name='usuario'),
]