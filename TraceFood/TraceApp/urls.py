from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', views.home , name= 'home'), 
   path('productos/', views.buscar_producto, name= 'buscar_producto'),
   path('escanear/', views.escanear_producto, name= 'escanear_producto'),
   path('gestion/', views.gestion, name= 'gestion'),
   path('inicio/', views.home_secundario, name= 'inicio'),
   path('nosotros/', views.nosotros, name= 'nosotros'),

   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
 