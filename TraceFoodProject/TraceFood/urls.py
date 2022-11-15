"""TraceFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from traceFoodApp import views as traceFoodAppViews

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', traceFoodAppViews.home , name= 'home'), 
    path('inicio/', traceFoodAppViews.home_secundario, name= 'inicio'),
    path('nosotros/', traceFoodAppViews.nosotros, name= 'nosotros'),
    path('productos/', traceFoodAppViews.productoSearch, name='buscar_producto'),
    path('escanear/', traceFoodAppViews.escanear, name='escanear_producto'), 
    path('login/', traceFoodAppViews.login , name= 'login'),
    path('gestion/<usuario_id>', traceFoodAppViews.gestion, name= 'gestion'),
    path('perfil/<usuario_id>', traceFoodAppViews.perfilView , name= 'perfil'),  
    path('escanear/<usuario_id>', traceFoodAppViews.escanear_productoR, name='escanear_productoR'), 
    path('producto/<usuario_id>', traceFoodAppViews.productoView, name='productoView'),
    path('productoEdit/<producto_id>', traceFoodAppViews.productoEdit, name='productoEdit'),
    path('productoForm/<usuario_id>', traceFoodAppViews.productoForm, name='productoForm'),
    path('res/<usuario_id>', traceFoodAppViews.resesView, name= 'resesView'),
    path('resEdit/<res_id>', traceFoodAppViews.resesEdit, name= 'resesEdit'),
    path('resForm/<usuario_id>', traceFoodAppViews.resesForm, name= 'resesForm'),
    path('proveedor/<usuario_id>', traceFoodAppViews.proveedorView, name='proveedorView'),
    path('proveedorForm/', traceFoodAppViews.proveedorForm, name='proveedorForm'),
    path('proveedorEdit/<usuario_id>', traceFoodAppViews.proveedorEdit, name='proveedorEdit'),
    path('recepcion/<usuario_id>', traceFoodAppViews.recepcionView, name='recepcionView'),
    path('recepcionForm/<usuario_id>', traceFoodAppViews.recepcionForm, name='recepcionForm'),
    path('recepcionEdit/<ficha_id>', traceFoodAppViews.recepcionEdit, name='recepcionEdit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)