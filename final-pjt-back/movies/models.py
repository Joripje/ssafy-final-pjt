from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=60)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()