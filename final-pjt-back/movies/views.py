from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def get_genre(request, movie_pk):
    movie =  Movie.objects.get(pk=movie_pk)
    serializer = MovieGenreSerializer(movie)

    return Response(serializer.data)


@api_view(['GET'])
def get_actors(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(reuqest, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = reuqest.user
    serializer = ReviewSerializer(data=reuqest.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie,user=user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_review(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    user = request.user
    if review.like_user.filter(pk=user.pk).exists():
        review.like_user.remove(user)
    else:
        review.like_user.add(user)
    serializer = WishMovieSerializer(review)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_wishlist(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    print(movie)
    user = request.user
    print(user)
    if movie.wish_user.filter(pk=user.pk).exists():
        movie.wish_user.remove(user)
    else:
        movie.wish_user.add(user)
    serializer = LikeReviewSerializer(movie)

    return Response(serializer.data)