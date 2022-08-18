from django.db import models
from django.urls import reverse
# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=64, help_text='Pon el nombre del director')

    def __str__(self):
        return self.name

class Genero(models.Model):
    name = models.CharField(max_length=64, help_text='Pon el nombre del genero')

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    name = models.CharField(max_length=64, help_text='Pon el nombre de la película')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=200, help_text='Pon aquí de que va la película')
    genre = models.ManyToManyField(Genero)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('pelicula-detail', args=[str(self.id)])