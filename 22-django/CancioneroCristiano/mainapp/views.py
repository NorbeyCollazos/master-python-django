from django.shortcuts import render, HttpResponse, redirect

from mainapp.models import Artistas, Canciones
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegistrarUsuraio

# Create your views here.

def index(request, nombre_artista=""):
    artistas = Artistas.objects.order_by('nombre')


    return render(request,'index.html',{
        'titulo': 'Cancionero Cristiano Letras Acordes y Música',
        'artistas': artistas,

    })

def index_filtro(request):

    if request.method == 'POST':
        nombre_artista = request.POST['nombre_artista']
        
    artistas = Artistas.objects.filter(nombre__contains=nombre_artista)



    return render(request,'index.html',{
        'titulo': 'Inicio',
        'artistas': artistas,

    })


def listado(request, artista):

    #canciones = Canciones.objects.all()
    canciones = Canciones.objects.filter(artista=artista)
    artista = Artistas.objects.get(nombre=artista)
    artistas = Artistas.objects.order_by('nombre')

    #canciones_sql = Canciones.objects.raw("SELECT * FROM mainapp_canciones WHERE artista="+str(artista))

    return render(request, 'listado_canciones.html',{
        'canciones': canciones,
        'artista': artista,
        'artistas': artistas,

    })


def listado_buscar(request, artista):

    #canciones = Canciones.objects.all()
    if request.method == 'POST':
        buscar_cancion = request.POST['buscar_cancion']

    query = Q(titulo__contains=buscar_cancion)
    query.add(Q(cancion__contains=buscar_cancion), Q.OR)
    query.add(Q(artista=artista), Q.AND)


    canciones = Canciones.objects.filter(query)
    artista = Artistas.objects.get(nombre=artista)
    artistas = Artistas.objects.order_by('nombre')

    

    #canciones_sql = Canciones.objects.raw("SELECT * FROM mainapp_canciones WHERE artista="+str(artista))

    return render(request, 'listado_canciones.html',{
        'canciones': canciones,
        'artista': artista,
        'artistas': artistas,

    })


def listado_general(request):

    if request.method == 'POST':
        buscar_cancion = request.POST['buscar_cancion_general']

    #canciones = Canciones.objects.all()
    canciones = Canciones.objects.filter(Q(titulo__contains=buscar_cancion)|Q(cancion__contains=buscar_cancion)|Q(artista__contains=buscar_cancion))
    artistas = Artistas.objects.order_by('nombre')

    total_canciones = Canciones.objects.count()
    total_artistas = Artistas.objects.count()
    
    #canciones_sql = Canciones.objects.raw("SELECT * FROM mainapp_canciones WHERE artista="+str(artista))

    return render(request, 'listado_general.html',{
        'canciones': canciones,
        'artistas': artistas,
        'total_canciones': total_canciones,
        'total_artistas': total_artistas

    })


def biografia(request, artista):

    artista = Artistas.objects.get(nombre=artista)

    return render(request, 'biografia.html',{
        'artista': artista,

    })



def ver_cancion(request, id_cancion):

    cancion = Canciones.objects.get(id=id_cancion)

    artista = cancion.artista
    canciones = Canciones.objects.filter(artista=artista)

    autor = cancion.autor
    letra = cancion.cancion
    letra2 = letra.replace('{', f'<b><span class="chord{str(autor)}">')
    letra_cancion = letra2.replace('}','</span></b>')

    return render(request, 'ver_cancion.html',{
        'cancion': cancion,
        'letra': letra_cancion,
        'canciones': canciones

    })


def registrar_usuario(request):

    formulario_registro = RegistrarUsuraio()

    if request.method == "POST":
        formulario_registro = RegistrarUsuraio(request.POST)

        if formulario_registro.is_valid():
            formulario_registro.save()

            return redirect('index')

    return render(request,'usuarios/registro.html',{
        'titulo': "Registro",
        'formulario_registro': formulario_registro
    })
