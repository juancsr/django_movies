import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status as codes
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer

APPLICATION_JSON = 'application/json'

@method_decorator(csrf_exempt, name='dispatch')
class MovieView(APIView):
    """
    Description
    ----------
    Class used to represents Movies endpoints

    Methods availables : GET, POST, PUT, DELETE
    """
    def get(self, request, *args, **kwargs):
        response = {}
        body = {
            'success': True,
            'data': []
        }
        params = { key: value for key, value in request.GET.items() }
        status = codes.HTTP_200_OK
        try:
            data = Movie.objects.all()
            print(data)
            serializer = MovieSerializer(data, many=True)
            body['data'] = serializer.data
        except Exception as e:
            status = codes.HTTP_400_BAD_REQUEST
            body['success'] = False
            print(e)
        
        #return HttpResponse(json.dumps(body), APPLICATION_JSON, status=status)
        return Response(body)
