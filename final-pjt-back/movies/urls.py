from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('<int:pk>/', views.movie_detail),
    path('<int:pk>/add_wishlist/', views.add_wishlist),
    path('<int:pk>/genre/', views.get_genre),
    path('<int:pk>/actors/', views.get_actors),
]