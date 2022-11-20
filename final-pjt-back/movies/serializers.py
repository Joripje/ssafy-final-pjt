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


class WishMovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username',)

    wish_user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'wish_user')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)


class LikeReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username',)
    
    like_user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'like_user')