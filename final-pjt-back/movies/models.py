from django.db import models

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
    genre_ids = models.ManyToManyField(Genre, related_name='genre_movie')
    actors = models.ManyToManyField(Actor, related_name='actor_movie')