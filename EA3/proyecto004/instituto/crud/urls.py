from . import views
from django.urls import path

urlpatterns = [
    path('genero', views.genero, name="genero"),
    path('marca', views.marca, name="marca"),
]
