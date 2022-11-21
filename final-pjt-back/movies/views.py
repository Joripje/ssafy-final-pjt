from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Count

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

# 리뷰 좋아요, 좋아요 개수 확인
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def like_review(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     if request.method == 'GET':
#         like_counts = Review.objects.annotate(like_user_count = Count('like_user', distinct=True))

#         like_count = like_counts.get(pk=review_pk)
#         serializer = ReviewLikeCountSerializer(like_count)
        
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         user = request.user
#         if review.like_user.filter(pk=user.pk).exists():
#             review.like_user.remove(user)
#         else:
#             review.like_user.add(user)
#         serializer = LikeReviewSerializer(review)

#         return Response(serializer.data)


# 리뷰 좋아요, 좋아요 개수 확인
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'POST':
        user = request.user
        if review.like_user.filter(pk=user.pk).exists():
            review.like_user.remove(user)
        else:
            review.like_user.add(user)
        # serializer = LikeReviewSerializer(review)

    # like_counts = Review.objects.annotate(like_user_count = Count('like_user', distinct=True))
    # like_count = like_counts.get(pk=review_pk)
    serializer = ReviewSerializer(review)

    return Response(serializer.data)


# 위시리스트 추가, 해당 영화를 위시리스트에 담은 사람
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def add_wishlist(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'POST':
        user = request.user
        if movie.wish_user.filter(pk=user.pk).exists():
            movie.wish_user.remove(user)
        else:
            movie.wish_user.add(user)

    wish_counts = Movie.objects.annotate(wish_user_count = Count('wish_user', distinct=True))
    wish_count = wish_counts.get(pk=movie_pk)

    serializer = WishMovieSerializer(wish_count)

    return Response(serializer.data)


# 배우 상세(출연작)
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorMovieSerializer(actor)

    return Response(serializer.data)


# 리뷰 조회
@api_view(['GET'])
def review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # like_counts = Review.objects.annotate(like_user_count = Count('like_user', distinct=True))
    # print(movie)
    serializer = MovieReviewSerializer(movie)

    # print(serializer.data)

    return Response(serializer.data)


# 개별 리뷰 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def rud_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        # review = Review.objects.get(pk=review_pk)
        serializer = ReviewSerializer(review)

        # like_counts = Review.objects.annotate(like_user_count = Count('like_user', distinct=True))
        # like_count = like_counts.get(pk=review_pk)
        # serializer = ReviewSerializer(like_count)

        return Response(serializer.data)

    elif request.method == 'PUT':
        if review.user == request.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        else:
            return Response('작성자가 아닙니다.')

    elif request.method == 'DELETE':
        if review.user == request.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('작성자가 아닙니다.')


#리뷰 조회
@api_view(['GET'])
def review_list(request, movie_pk):
    pass