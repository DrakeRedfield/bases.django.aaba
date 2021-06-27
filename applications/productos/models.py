from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=50)
    precio = models.FloatField(default = 0)
    peso = models.FloatField(default = 0.5)
    marca = models.CharField(max_length=50)
    descripcion = models.TextField(default='')
    categoria = models.ForeignKey( Categoria, on_delete = models.CASCADE)

    def __str__(self):
        return (f'{self.marca} {self.name}')