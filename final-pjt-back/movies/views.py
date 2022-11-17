from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def get_genre(request, pk):
    movie =  Movie.objects.get(pk=pk)
    serializer = MovieGenreSerializer(movie)

    return Response(serializer.data)


@api_view(['GET'])
def get_actors(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieActorSerializer(movie)

    return Response(serializer.data)


@api_view(['GET'])
def get_movielist(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_actorlist(request):
    actor = Actor.objects.all()
    serializer = ActorSerializer(actor, many=True)

    return Response(serializer.data)


# @api_view(['POST'])
# def add_wishlist(request, pk):
#     print(123123123)
#     movie = Movie.objects.get(pk=pk)
#     print(movie)
#     user = request.user
#     print(user)
#     if movie.wish_user.filter(pk=2).exists():
#         movie.wish_user.remove(2)
#     else:
#         movie.wish_user.add(2)
#     serializer = WishMovieSerializer(movie)

#     return Response(serializer.data)