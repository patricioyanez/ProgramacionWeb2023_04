from django.shortcuts import render
from .models import Genero
# Create your views here.

def genero(request):
    generos = Genero.objects.all() # select * from Genero
    context = {"generos": generos}
    return render(request, 'genero.html', context)