from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
