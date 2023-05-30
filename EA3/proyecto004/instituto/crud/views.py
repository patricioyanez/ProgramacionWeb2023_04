from django.shortcuts import render
from .models import Genero, Marca
# Create your views here.

"""def genero(request):
    generos = Genero.objects.all() # select * from Genero
    context = {"generos": generos}
    return render(request, 'genero.html', context)"""

def genero(request):
    context = {}

    if request.method == 'POST':
        id      = int("0" + request.POST['id'])
        nombre  = request.POST['nombre']

        # print(id, nombre)
        if 'Grabar' in request.POST: # fue presionado el boton Grabar
            if id == 0: # insert
                Genero.objects.create(nombre=nombre)
            else:
                item = Genero.objects.get(pk=id)
                item.nombre = nombre
                item.save()
        elif 'Listar' in request.POST:
            listado = Genero.objects.all()
            context = {'listado': listado}




    return render(request, 'genero.html', context)


def marca(request):
    marcas = Marca.objects.all() # select * from Genero
    context = {"marcas": marcas}
    return render(request, 'marca.html', context)