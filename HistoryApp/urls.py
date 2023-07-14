from django.urls import path, include
from HistoryApp import views 

urlpatterns = [
   path('', views.home, name='Inicio'),
   path('Temas/', views.temas, name='Temas'),
   path('Usuarios/', views.usuarios, name='Usuarios'),
   path('Admin/', views.admins, name='Admin'),
   path('Membresia/', views.membresia, name='Membresia'),
   # path('Formularios/', views.formulario, name='Formularios'),
   path('AdminFormulario/', views.adminFormulario, name='AdmiFormulario'),
   path('BusquedaTema/', views.busquedaTema, name='BusquedaTema'),
   path('Busqueda/', views.busqueda),
]