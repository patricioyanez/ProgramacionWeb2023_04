from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero= models.AutoField(db_column='idGenero', primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    rut = models.IntegerField(unique=True, null=False, blank=False)
    dv = models.CharField(max_length=1, null=False, blank=False, default="")
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=20, null=False, blank=False)
    genero = models.ForeignKey(Genero, db_column='idGenero', 
                                on_delete=models.CASCADE, null=False, blank=False)
    fechaNacimiento = models.DateField(null=False, blank=False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + " " + self.apellido






class Marca(models.Model):
    id_marca= models.AutoField(db_column='idMarca', primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    id_categoria= models.AutoField(db_column='idCategoria', primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre

## Marca
## Categoria

# PASOS:
# 1.- para preparar la migración:
# py manage.py makemigrations crud
# 2.- hacer migracion
# py manage.py migrate crud

### otras clases que representan los modelos
