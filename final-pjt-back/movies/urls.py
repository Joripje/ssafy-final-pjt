from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('detail/<int:pk>/', views.movie_detail)
]