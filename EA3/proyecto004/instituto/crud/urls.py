from . import views
from django.urls import path

urlpatterns = [
    path('genero', views.genero, name="genero"), # 127.0.0.1:8000/crud/genero
    path('marca', views.marca, name="marca"), # ejercicio crear form para marca y categoria
    path('categoria', views.categoria, name="categoria"), 
    path('clienteForm', views.clienteForm, name="clienteForm"), 
]
