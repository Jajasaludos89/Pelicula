from django.db import models

class Cine(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    capacidad_total = models.PositiveIntegerField()
    numero_salas = models.PositiveIntegerField()

    logo = models.FileField(upload_to='cine_logo', null=True, blank=True)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    fecha_funcion = models.DateField()
    cine = models.ForeignKey(Cine, on_delete=models.CASCADE, related_name='peliculas')

    logo = models.FileField(upload_to='peli_logo', null=True, blank=True)
    archivo = models.FileField(upload_to='peli_archivos', null=True, blank=True)
