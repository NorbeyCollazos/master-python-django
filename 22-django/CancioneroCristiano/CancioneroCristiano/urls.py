"""CancioneroCristiano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.index, name='index'),
    path('buscando-artista',mainapp.views.index_filtro, name='index_filtro'),
    path('listado/<str:artista>',mainapp.views.listado, name='listado'),
    path('listado_buscar/<str:artista>',mainapp.views.listado_buscar, name='listado_buscar'),
    path('listado_general',mainapp.views.listado_general, name='listado_general'),
    path('biografia/<str:artista>',mainapp.views.biografia, name='biografia'),
    path('cancion/<int:id_cancion>',mainapp.views.ver_cancion, name='cancion'),

    path('registrar/',mainapp.views.registrar_usuario, name='registrar_usuario'),
]
