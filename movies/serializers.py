from rest_framework import serializers

from movies.models import Pelicula

class PeliculaSerializer(serializers.ModelSerializer):

    pais = serializers.CharField()
    
    class Meta:
        model = Pelicula
        fields = ('titulo', 'pais')


