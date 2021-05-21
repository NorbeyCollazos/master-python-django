from django.db import models

# Create your models here.
class Artistas(models.Model):
    imagen = models.CharField(max_length=250)
    biografia = models.TextField()
    nombre = models.CharField(max_length=100)
    num_canciones = models.IntegerField(10)
    estado = models.CharField(max_length=30, null=True)

class Canciones(models.Model):
    titulo = models.CharField(max_length=150, null=True)
    cancion = models.TextField(null=True)
    autor = models.CharField(max_length=10, null=True)
    artista = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=250, null=True)
