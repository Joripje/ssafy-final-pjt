from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class GenreNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('__all__')


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
            fields = '__all__'

    wish_user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields ='__all__'