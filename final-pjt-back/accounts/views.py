from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from movies.models import *
from .serializers import *
from collections import OrderedDict

# 추천기능 import
import json
import pandas as pd
# import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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
    genre_dict = {
        12: '모험',
        14: '판타지',
        16: '애니메이션',
        18: '드라마',
        27: '공포',
        28: '액션',
        35: '코미디',
        36: '역사',
        37: '서부',
        53: '스릴러',
        80: '범죄',
        99: '다큐멘터리',
        878: 'SF',
        9648: '미스터리',
        10402: '음악',
        10749: '로맨스',
        10751: '가족',
        10752: '전쟁',
        10770: 'TV 영화',
    }

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

    prefer_color = {
        1: '#c94c44',
        2: '#886b68',
        3: '#60b2a0',
        4: '#cfa146',
        5: '#212121',
        6: '#00796b',
        7: '#e040fb',
        8: '#795548',
        9: '#388e3c',
        10: '#f8bbd0',
        11: '#00BCD4',
        12: '#CDDC39',
        13: '#BDBDBD',
        14: '#7C4DFF',
        15: '#800020',
        16: '#ffe4e1',
        17: '#e1fcff',
        18: '#00616b',
        19: '#0a006b',
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
             

    val = set()
    for key, value in prefer_dict.items():
        val.add(value)

    val = sorted(val, reverse=True)
    
    user_prefer_genre = {}
    label = []
    color = []
    scale =[]

    for v in val:
        for key, value in prefer_dict.items():
            
            if value == v and v:
                label.append(genre_dict[key])
                color.append(prefer_color[len(label)])
                scale.append(value)
                
        if len(user_prefer_genre) >= 3:
            break
    user_prefer_genre['label'] = label
    user_prefer_genre['color'] = color
    user_prefer_genre['scale'] = scale

    print(user_prefer_genre)

    return Response(user_prefer_genre)

# 장르기반 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
    # 장르딕셔너리
    genre_dict = {
        12: 'adventure',
        14: 'fantasy',
        16: 'animation',
        18: 'drama',
        27: 'horror',
        28: 'action',
        35: 'comedy',
        36: 'historical',
        37: 'western',
        53: 'thriller',
        80: 'crime',
        99: 'documentary',
        878: 'sf',
        9648: 'mistery',
        10402: 'musical',
        10749: 'romance',
        10751: 'family',
        10752: 'war',
        10770: 'tvmovie',
    }
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
    val = set()
    for key, value in prefer_dict.items():
        val.add(value)

    val = sorted(val, reverse=True)
    
    user_prefer_genre = []
    
    for v in val:
        for key, value in prefer_dict.items():
            
            if value == v and v:
                user_prefer_genre.append(genre_dict[key])
                
        if len(user_prefer_genre) >= 3:
            break

    with open('movies/fixtures/movies.json', 'r', encoding='UTF8') as file:
        json_ = json.loads(file.read())   

    json_data = []

    # 사용자 선호 장르를 데이터프레임 0번 인덱스에 넣음
    data_dict = {}
    data_dict['pk'] = 0
    data_dict['title'] = '사용자'
    data_dict['vote_count'] = 0
    data_dict['vote_average'] = 0
    data_dict['genres'] = user_prefer_genre

    json_data.append(data_dict)

    for data in json_:
        
        data_dict = {}
        data_dict['pk'] = data['pk']
        data_dict['title'] = data['fields']['title']
        data_dict['vote_count'] = data['fields']['vote_count']
        data_dict['vote_average'] = data['fields']['vote_average']
        genres = []
        for genre in data['fields']['genres']:
            genres.append(genre_dict[genre])
    #         genres.append(str(genre))
        data_dict['genres'] = genres
    #     data_dict['actors'] = data['fields']['actors']
        
        json_data.append(data_dict)
        
    df = pd.DataFrame(json_data)

    df['genres'] = df['genres'].apply(lambda x:(' ').join(x))

    # tfidf_vector = TfidfVectorizer(ngram_range=(1,2))
    # genre_matrix = tfidf_vector.fit_transform(df['genres']).toarray()

    count_vect = CountVectorizer(ngram_range=(1,2))
    genre_matrix = count_vect.fit_transform(df['genres'])

    cosine_similarity_matrix = cosine_similarity(genre_matrix)
    sim_list = [0] * len(df)
    for idx in cosine_similarity_matrix.argsort()[:, ::-1][0]:
        sim_list[idx] = cosine_similarity_matrix[0][idx]

    df['similarity'] = sim_list

    m = df['vote_count'].quantile(0.5)
    C = df['vote_average'].mean()

    def weighted_score(data, m = m, C = C):
        v = data['vote_count']
        R = data['vote_average']
        
        return ((v / (v + m)) * R) + ((m / (m + v)) * C)

    df['weighted_score'] = df.apply(weighted_score, axis=1)
    recommend_df = df[1:].sort_values(by=['similarity', 'weighted_score'], ascending=False)

    # recommand_df = df[1:].sort_values(by='similarity', ascending=False)
    

    recommend_list = []

    for id in recommend_df['pk']:
        movie = Movie.objects.get(pk=id)
        serializer = RecommendSerializer(movie)
        recommend_list.append(serializer.data)
        if len(recommend_list) == 20:
            break

    return Response(recommend_list)