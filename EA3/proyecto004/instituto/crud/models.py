from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero= models.AutoField(db_column='idGenero', primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre
    
