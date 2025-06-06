from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.listar_cines),

    path('cines', views.listar_cines),
    path('nuevoCine', views.nuevo_cine),
    path('guardarCine', views.guardar_cine),
    path('editarCine/<id>', views.editar_cine),
    path('actualizarCine', views.actualizar_cine),
    path('eliminarCine/<id>', views.eliminar_cine),

    path('peliculas', views.listar_peliculas),
    path('nuevaPelicula', views.nueva_pelicula),
    path('guardarPelicula', views.guardar_pelicula),
    path('editarPelicula/<id>', views.editar_pelicula),
    path('actualizarPelicula', views.actualizar_pelicula),
    path('eliminarPelicula/<id>', views.eliminar_pelicula),
]
