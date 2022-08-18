from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    num_peliculas = Pelicula.objects.all().count()
    num_generos = Genero.objects.all().count()
    num_directores = Director.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_peliculas': num_peliculas,
            'num_directores': num_directores,
            'num_generos': num_generos
        }
    )