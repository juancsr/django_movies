import json

from django.http import HttpResponse
from django.db.models import Q
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
            new_movie = Pelicula.objects.create(titulo=data['titulo'], pais=Pais.objects.get(id=data['pais']))
            new_movie.save()
            serializer = PeliculaSerializer(new_movie)
            response['data'] = serializer.data
        except Exception as e:
            response['success'] = False
            print(e)

        return Response(response)
    
    def put(self, request, *args, **kwargs):
        response = { 'success': True }
        try:
            id = kwargs['pk']
            data = request.data
            movie = Pelicula.objects.get(id=id)
            movie.titulo = data['titulo']
            if movie.pais.pk != data['pais']:
                movie.pais = Pais.objects.get(pk=data['pais'])
            movie.save()
            serializer = PeliculaSerializer(movie)
            response['data'] = serializer.data
        except Exception as e:
            response['success'] = False
            print(e)
        
        return Response(response)

    def delete(self, request, *args, **kwargs):
        response = { 'success': True }
        try:
            id = kwargs['pk']
            Pelicula.objects.get(id=id).delete
        except Exception as e:
            response['success'] = False
            print(e)
        
        return Response(response)

class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'success': True}
        try:
            query = request.query_params['query']
            filter = Q(titulo__icontains=query) | Q(pais__nombre__icontains=query) | Q(calificacion=int(query))
            data = Pelicula.objects.filter(filter)
            serializer = PeliculaSerializer(data, many=True)
            response['data'] = serializer.data
        except ValueError:
            filter = Q(titulo__icontains=query) | Q(pais__nombre__icontains=query)
            data = Pelicula.objects.filter(filter)
            serializer = PeliculaSerializer(data, many=True)
            response['data'] = serializer.data
        except KeyError as e:
            response['success'] = False
            print(e)
        
        return Response(response)

class SummaryView(APIView):

    def get(self, request):
        response = {'success': True}
        CLAVE_TEMPLATE = 'count_calificacion_'
        try:
            response['data'] = []
            paises = Pais.objects.all().values_list('nombre')
            for pais in paises:
                count_paises = Pelicula.objects.filter(pais__nombre=pais[0])
                data = { 'pais': pais[0], 'count_pais': count_paises.count() }

                for i in range(1,6):
                    clave = CLAVE_TEMPLATE+str(i)
                    data[clave] = 0
                
                for pelicula in count_paises.values_list('calificacion'):
                    clave = CLAVE_TEMPLATE+str(pelicula[0])
                    data[clave] = data[clave] + 1

                response['data'].append(data)
            
        except KeyError as ke:
            response['success'] = False
            print(ke)
        except Exception as e:
            response['success'] = False
            print(e)
        return Response(response)

class TopView(APIView):

    def get(self, request):
        response = {'success': True}
        try:
            movies = Pelicula.objects.order_by('-calificacion')[:5]
            serializer = PeliculaSerializer(movies, many=True)
            response['data'] = serializer.data
        except Exception as e:
            response['success'] = False
            print(e)
        return Response(response)
        

