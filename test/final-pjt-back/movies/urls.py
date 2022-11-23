from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('<int:movie_pk>/', views.movie_detail),  # 영화의 디테일 페이지
    path('<int:movie_pk>/add_wishlist/', views.add_wishlist),  # 위시리스트 추가
    path('<int:movie_pk>/genre/', views.get_genre),  # 해당 영화의 장르 리스트
    path('<int:movie_pk>/actors/', views.get_actors),  # 해당 영화의 배우 리스트
    path('movie_list/', views.get_movielist),  # 모든 영화 리스트 가져오기
    path('actor_list/', views.get_actorlist),  # 모든 배우 리스트 가져오기
    path('actor_list/<int:actor_pk>/', views.actor_detail),  # 배우 출연작?
    path('<int:movie_pk>/create_review/', views.create_review),  # 리뷰 작성
    path('<int:movie_pk>/review/', views.review),  # 리뷰 확인
    path('review/<int:review_pk>/', views.rud_review),  # 리뷰 확인, 수정, 삭제
    path('review/<int:review_pk>/like/', views.like_review),  # 리뷰 좋아요, 좋아요 개수 확인
]