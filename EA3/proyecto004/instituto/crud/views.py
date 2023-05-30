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
                context = {'exito': 'Los datos fueron guardados con éxito.'}
            else: # update
                try:
                    item = Genero.objects.get(pk=id)
                    item.nombre = nombre
                    item.save()
                    context = {'exito': 'Los datos fueron guardados con éxito.'}
                except:                    
                    context = {'error': 'Error en la modificación.'}
        elif 'Listar' in request.POST: # select * from genero
            listado = Genero.objects.all()
            context = {'listado': listado}
        elif 'Buscar' in request.POST: # select * from genero where...
            try:
                item = Genero.objects.get(pk=id)
                context = {'item': item}
            except:
                context = {'error': 'Error en la búsqueda.'}
        elif 'Eliminar' in request.POST: # delete
            try:
                item = Genero.objects.get(pk=id)
                item.delete()
                context = {'exito': 'Registro eliminado.'}
            except:
                context = {'error': 'Error en la eliminación.'}




    return render(request, 'genero.html', context)



### ejercicio: Crear crud con plantillas para el modelo MARCA
def marca(request):
    marcas = Marca.objects.all() # select * from Genero
    context = {"marcas": marcas}
    return render(request, 'marca.html', context)