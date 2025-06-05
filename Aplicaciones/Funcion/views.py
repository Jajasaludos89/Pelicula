from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cine, Pelicula
import os

#Cines

def listar_cines(request):
    cines = Cine.objects.all()
    return render(request, "inicio_cine.html", {"cines": cines})

def nuevo_cine(request):
    return render(request, "nuevo_cine.html")

def guardar_cine(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        direccion = request.POST["direccion"]
        ciudad = request.POST["ciudad"]
        capacidad_total = request.POST["capacidad_total"]
        numero_salas = request.POST["numero_salas"]

        logo = request.FILES.get("logo")

        Cine.objects.create(
            nombre=nombre,
            direccion=direccion,
            ciudad=ciudad,
            capacidad_total=capacidad_total,
            numero_salas=numero_salas,
            logo=logo
        )
        messages.success(request, "Cine GUARDADO exitosamente")
        return redirect("/cines")

def editar_cine(request, id):
    cine = Cine.objects.get(id=id)
    return render(request, "editar_cine.html", {"cine": cine})

def actualizar_cine(request):
    if request.method == "POST":
        id = request.POST["id"]
        cine = Cine.objects.get(id=id)
        cine.nombre = request.POST["nombre"]
        cine.direccion = request.POST["direccion"]
        cine.ciudad = request.POST["ciudad"]
        cine.capacidad_total = request.POST["capacidad_total"]
        cine.numero_salas = request.POST["numero_salas"]

        logo = request.FILES.get("logo")
        if logo:
            if cine.logo and os.path.isfile(cine.logo.path):
                os.remove(cine.logo.path)
            cine.logo = logo

        cine.save()
        messages.success(request, "Cine ACTUALIZADO exitosamente")
        return redirect("/cines")

def eliminar_cine(request, id):
    cine = Cine.objects.get(id=id)
    if cine.logo and os.path.isfile(cine.logo.path):
        os.remove(cine.logo.path)
    cine.delete()
    messages.success(request, "Cine ELIMINADO exitosamente")
    return redirect("/cines")

#Peliculas

def listar_peliculas(request):
    peliculas = Pelicula.objects.select_related("cine")
    return render(request, "inicio_pelicula.html", {"peliculas": peliculas})

def nueva_pelicula(request):
    cines = Cine.objects.all()
    return render(request, "nueva_pelicula.html", {"cines": cines})

def guardar_pelicula(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        genero = request.POST["genero"]
        duracion = request.POST["duracion"]
        fecha_funcion = request.POST["fecha_funcion"]
        cine_id = request.POST["cine"]
        cine = Cine.objects.get(id=cine_id)

        logo = request.FILES.get("logo")
        archivo = request.FILES.get("archivo")

        Pelicula.objects.create(
            titulo=titulo,
            genero=genero,
            duracion=duracion,
            fecha_funcion=fecha_funcion,
            cine=cine,
            logo=logo,
            archivo=archivo
        )
        messages.success(request, "Película GUARDADA exitosamente")
        return redirect("/peliculas")

def editar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    cines = Cine.objects.all()
    return render(request, "editar_pelicula.html", {"pelicula": pelicula, "cines": cines})

def actualizar_pelicula(request):
    if request.method == "POST":
        id = request.POST["id"]
        pelicula = Pelicula.objects.get(id=id)
        pelicula.titulo = request.POST["titulo"]
        pelicula.genero = request.POST["genero"]
        pelicula.duracion = request.POST["duracion"]
        pelicula.fecha_funcion = request.POST["fecha_funcion"]
        cine_id = request.POST["cine"]
        pelicula.cine = Cine.objects.get(id=cine_id)

        logo = request.FILES.get("logo")
        archivo = request.FILES.get("archivo")

        if logo:
            if pelicula.logo and os.path.isfile(pelicula.logo.path):
                os.remove(pelicula.logo.path)
            pelicula.logo = logo
        if archivo:
            if pelicula.archivo and os.path.isfile(pelicula.archivo.path):
                os.remove(pelicula.archivo.path)
            pelicula.archivo = archivo

        pelicula.save()
        messages.success(request, "Película ACTUALIZADA exitosamente")
        return redirect("/peliculas")

def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    if pelicula.logo and os.path.isfile(pelicula.logo.path):
        os.remove(pelicula.logo.path)
    if pelicula.archivo and os.path.isfile(pelicula.archivo.path):
        os.remove(pelicula.archivo.path)
    pelicula.delete()
    messages.success(request, "Película ELIMINADA exitosamente")
    return redirect("/peliculas")
