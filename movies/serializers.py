from rest_framework import serializers

from movies.models import Pelicula, Pais

class PeliculaSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='pais.nombre')
    class Meta:
        model = Pelicula
        fields = ('titulo', 'country_name')
