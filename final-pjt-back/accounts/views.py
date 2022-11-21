from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from movies.models import *
from .serializers import *
from collections import OrderedDict

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = ProfileSerializer(user)

    return Response(serializer.data)

# 장르 선호도
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genre_prefer(request):
    prefer_dict = {
        12: 0,
        14: 0,
        16: 0,
        18: 0,
        27: 0,
        28: 0,
        35: 0,
        36: 0,
        37: 0,
        53: 0,
        80: 0,
        99: 0,
        878: 0,
        9648: 0,
        10402: 0,
        10749: 0,
        10751: 0,
        10752: 0,
        10770: 0,
    }
    user = request.user

    serializer = PreferGenreSerializer(user)
    genres = serializer.data['review_user']
    
    for genre in genres:
        genre = dict(OrderedDict(genre))
        rating = genre['rate']
        genre_list = dict(OrderedDict(dict(OrderedDict(genre['movie']))))['genres']
        
        for gen in genre_list:
            prefer_dict[gen] += 1
             
    print(prefer_dict)
    return Response(serializer.data)
    