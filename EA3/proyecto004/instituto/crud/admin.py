from django.contrib import admin
from .models import Genero, Categoria, Marca, Cliente
# Register your models here.

admin.site.register(Genero)
admin.site.register(Categoria)
admin.site.register(Marca)

# configurar que columnas se van a mostrar
# configurar filtros
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'genero']
    list_filter  = ['genero', 'apellido']

admin.site.register(Cliente, ClienteAdmin)