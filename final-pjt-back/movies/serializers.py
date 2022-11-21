from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


# class MovieListSerializer(serializers.ModelSerializer):

#     class Meta:
#         models = Movie
#         fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class GenreNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('genres',)


class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'

    
class MovieActorSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('actors',)

# 위시리스트 유저
class WishMovieSerializer(serializers.ModelSerializer):

    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = get_user_model()
    #         fields = ('id', 'username',)

    # wish_user = UserSerializer(many=True, read_only=True)
    wish_user_count = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('id', 'wish_user_count', 'wish_user')


class ReviewSerializer(serializers.ModelSerializer):

    like_user_count = serializers.IntegerField(source='like_user.count', read_only=True)
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)
        ordering = ['-like_user_count']

    


class LikeReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username',)
    
    like_user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'like_user')


# 배우의 출연작
class ActorMovieSerializer(serializers.ModelSerializer):

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path')

    actor_movie = MovieListSerializer(many=True)

    class Meta:
        model = Actor
        fields = '__all__'


# 영화에 연결된 리뷰
class MovieReviewSerializer(serializers.ModelSerializer):

    movie_review = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'movie_review',)

# # 영화에 연결된 리뷰
# class MovieReviewSerializer(serializers.HyperlinkedModelSerializer):

#     movie_review = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = ('id', 'title', 'movie_review',)

#     def get_movie_review(self, instance):
#         reviews = instance.movie_review.all().order_by('-like_user')
#         return ReviewSerializer(reviews, many=True).data


# # 리뷰 좋아요 개수
# class ReviewLikeCountSerializer(serializers.ModelSerializer):

#     like_user_count = serializers.IntegerField()

#     class Meta:
#         model = Review
#         fields = ('id', 'like_user_count', 'rate', 'content', 'like_user')