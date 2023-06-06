from django.shortcuts import render
# importar los modelos
from .models import Genero, Marca,Categoria

# importar los decoradores de auth de django
from django.contrib.auth.decorators import login_required

#importar los Forms (django Forms)
from .forms import ClienteForm


# ejercicio: Crear crud con plantillas para el modelo MARCA
# Ejercicio 2: Crear el modelo y el Django Forms para el Producto
# Ejercicio 3: Preguntar antes de logout, si esta seguro de hacerlo

# Create your views here.

"""def genero(request):
    generos = Genero.objects.all() # select * from Genero
    context = {"generos": generos}
    return render(request, 'genero.html', context)"""

@login_required
def menu(request):
    return render(request, 'menu.html')

@login_required
def genero(request):
    context = {}

    if request.method == 'POST':
        id      = int("0" + request.POST['id'])
        nombre  = request.POST['nombre']

        # print(id, nombre)
        if 'Grabar' in request.POST: # fue presionado el boton Grabar
            if len(nombre) == 0:
                context = {'error': 'Error en el ingreso de datos.'}
            else:
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


@login_required
def marca(request):
    context = {}

    if request.method == 'POST':
        id      = int("0" + request.POST['id'])
        nombre  = request.POST['nombre']

        # print(id, nombre)
        if 'Grabar' in request.POST: # fue presionado el boton Grabar
            if len(nombre) == 0:
                context = {'error': 'Error en el ingreso de datos.'}
            else:
                if id == 0: # insert
                    Marca.objects.create(nombre=nombre)
                    context = {'exito': 'Los datos fueron guardados con éxito.'}
                else: # update
                    try:
                        item = Marca.objects.get(pk=id)
                        item.nombre = nombre
                        item.save()
                        context = {'exito': 'Los datos fueron guardados con éxito.'}
                    except:                    
                        context = {'error': 'Error en la modificación.'}
            
        elif 'Listar' in request.POST: # select * from genero
            listado = Marca.objects.all()
            context = {'listado': listado}
        elif 'Buscar' in request.POST: # select * from genero where...
            try:
                item = Marca.objects.get(pk=id)
                context = {'item': item}
            except:
                context = {'error': 'Error en la búsqueda.'}
        elif 'Eliminar' in request.POST: # delete
            try:
                item = Marca.objects.get(pk=id)
                item.delete()
                context = {'exito': 'Registro eliminado.'}
            except:
                context = {'error': 'Error en la eliminación.'}
    return render(request, 'marca.html', context)

@login_required
def categoria(request):
    context = {}

    if request.method == 'POST':
        id      = int("0" + request.POST['id'])
        nombre  = request.POST['nombre']

        # print(id, nombre)
        if 'Grabar' in request.POST: # fue presionado el boton Grabar
            if len(nombre) == 0:
                context = {'error': 'Error en el ingreso de datos.'}
            else:
                if id == 0: # insert
                    Categoria.objects.create(nombre=nombre)
                    context = {'exito': 'Los datos fueron guardados con éxito.'}
                else: # update
                    try:
                        item = Categoria.objects.get(pk=id)
                        item.nombre = nombre
                        item.save()
                        context = {'exito': 'Los datos fueron guardados con éxito.'}
                    except:                    
                        context = {'error': 'Error en la modificación.'}
            
        elif 'Listar' in request.POST: # select * from genero
            listado = Categoria.objects.all()
            context = {'listado': listado}
        elif 'Buscar' in request.POST: # select * from genero where...
            try:
                item = Categoria.objects.get(pk=id)
                context = {'item': item}
            except:
                context = {'error': 'Error en la búsqueda.'}
        elif 'Eliminar' in request.POST: # delete
            try:
                item = Categoria.objects.get(pk=id)
                item.delete()
                context = {'exito': 'Registro eliminado.'}
            except:
                context = {'error': 'Error en la eliminación.'}
    return render(request, 'categoria.html', context)

@login_required
def clienteForm(request):
    context = {}
    if request.method == 'POST':
        if 'Grabar' in request.POST:
            form = ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                context = {'exito': 'Los datos fueron guardados con éxito.', 'form' : ClienteForm()}
            else:
                context = {'error': 'Error en el ingreso de datos.'}
    else:
        context = { 'form' : ClienteForm()}
    return render(request, 'clienteForm.html', context)