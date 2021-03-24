from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Country: table for movies
class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

# Movie: movie info
class Movie(models.Model):
    title = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

# Score: individual movie's score
class Score(models.Model):
    value = models.PositiveSmallIntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  
    def __str__(self):
        return self.valor