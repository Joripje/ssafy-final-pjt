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
    wish_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movie', blank=True)  # 해당 영화를 위시리스트에 추가한 사람들


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_review', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='review_user', on_delete=models.CASCADE)  # 작성자
    rate = models.IntegerField()  # 평점
    content = models.TextField(blank=True, null=True)  # 내용, 안적어도 됨
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review', blank=True)  # 해당 리뷰를 좋아하는 사람들