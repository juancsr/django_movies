from rest_framework import serializers

from movies.models import Movie

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)

    def create(self, data):
        return Movie.objects.create(**data)