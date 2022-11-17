from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    

class Actor(models.Model):
    name = models.CharField(max_length=50)
    profile_path = models.TextField(null=True)


class Movie(models.Model):
    title = models.CharField(max_length=60)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='genre_movie')
    actors = models.ManyToManyField(Actor, related_name='actor_movie')
    wish_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movie', blank=True)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.IntegerField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
