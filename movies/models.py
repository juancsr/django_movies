from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Country: table for movies
class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Movie: movie info
class Pelicula(models.Model):
    titulo = models.CharField(max_length=250)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    calificacion = models.PositiveSmallIntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self):
        return self.titulo

# Score: individual movie's score
class Puntuacion(models.Model):
    valor = models.PositiveSmallIntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)  

    def __str__(self):
        return self.valor
