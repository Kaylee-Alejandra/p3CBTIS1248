from django.urls import path
from . import views
urlpatterns= [
    path("",views.index,name="index"), 
    path("usuarios/",views.usuarios,name="usuarios"), 
    path("empleado/",views.empleados,name="empleado"), 
    path("instrumentos/",views.instrumentos,name="instrumentos"), 
    path("sucursales/",views.sucursales,name="sucursales"), 
]
