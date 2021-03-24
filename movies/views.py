import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status as codes
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response

from movies.models import Pelicula, Pais
from movies.serializers import PeliculaSerializer

class MovieView(APIView):
    """
    Description.
    ----------
    Class used to represents Movies endpoints

    Methods availables : GET, POST, PUT, DELETE
    """
    def get(self, request, *args, **kwargs):
        response = { 'success': True }
        try:
            id = kwargs['pk']
            data = Pelicula.objects.get(id=id)
            serializer = PeliculaSerializer(data)
            response['data'] = serializer.data
        except KeyError: ## Cuando no encuentra pk en kwargs
            data = Pelicula.objects.all()
            serializer = PeliculaSerializer(data, many=True)
            response['data'] = serializer.data
        except Exception as e:
            response['success'] = False
            print(e)
        return Response(response)

    def post(self, request, *args, **kwargs):
        response = { 'success': True }
        try:
            data = request.data
            serializer = PeliculaSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                saved = serializer.save()
                response['data'] = saved
        except Exception as e:
            response['success'] = False
            print(e)

        return Response(response)
