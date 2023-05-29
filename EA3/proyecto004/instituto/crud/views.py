from django.shortcuts import render
from .models import Genero, Marca
# Create your views here.

def genero(request):
    generos = Genero.objects.all() # select * from Genero
    context = {"generos": generos}
    return render(request, 'genero.html', context)

def marca(request):
    marcas = Marca.objects.all() # select * from Genero
    context = {"marcas": marcas}
    return render(request, 'marca.html', context)