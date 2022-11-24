from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import *
from movies.serializers import *

class MovieTitleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', "backdrop_path")

class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'genres', 'poster_path', 'overview')



    class ReviewSerializer(serializers.ModelSerializer):

        movie = MovieTitleSerializer()

        class Meta:
            model = Review
            fields = ('id', 'movie', 'rate', 'content')

    wish_movie = MovieSerializer(many=True)
    review_user = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

class PreferGenreSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):

        class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('genres', )

        movie = MovieSerializer()

        class Meta:
            model = Review
            fields = ('id', 'movie', 'rate',)

    review_user = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('review_user',)

class RecommendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'