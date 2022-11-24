import requests
import json
import re

def new_movie(pk):
    movie_dict = {}

    api_key = 'c77ef5df652e2127c8855d6cae700acb'

    base_url = f'https://api.themoviedb.org/3/movie/{pk}?api_key={api_key}&language=ko-KR'
    res = requests.get(base_url).json()
    
    movie_dict['movie'] = res

    actors = []
    credit_url = f'https://api.themoviedb.org/3/movie/{res["id"]}/credits?api_key={api_key}&language=ko-KR'
    res_credit = requests.get(credit_url).json()['cast']

    for actor in res_credit:
        if actor['order'] == 10:
            break
        detail_url = f'https://api.themoviedb.org/3/credit/{actor["credit_id"]}?api_key={api_key}'
        actors.append(requests.get(detail_url).json()['person']['id'])

    movie_dict['movie_actors'] = actors

    data = []
    for actor_id in actors:
        flag = 1
        url = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={api_key}&language=ko-KR'
        response = requests.get(url).json()
        also_known_as = response['also_known_as']
        for known in also_known_as:
            name = re.compile('[가-힣]+').findall(known)
            if name:
                full_name = name[0]
                if len(name) > 1:
                    for i in range(1, len(name)):
                        full_name = full_name + ' ' + name[i]
                actor_dict = {
                    'model': 'movies.actor',
                    'pk': actor_id,
                    'fields': {
                        'name': full_name,
                        'profile_path': response.get('profile_path')
                    }
                }
                data.append(actor_dict)
                
                flag = 0
                break
        if flag:
            actor_dict = {
                'model': 'movies.actor',
                'pk': actor_id,
                'fields': {
                    'name': response.get('name'),
                    'profile_path': response.get('profile_path')
                }
            }
            data.append(actor_dict)
            
        movie_dict['actors'] = data
    print(movie_dict['actors'])
    return movie_dict