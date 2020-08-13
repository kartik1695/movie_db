from django.shortcuts import render
from django.http import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from moviedb.models import Genre , Movie
from moviedb.serializer import MovieSerializer
from rest_framework.permissions import IsAuthenticated
import json
# Create your views here.


def get_movie(request):
    if request.method == "GET":
        if request.GET.get('movie'):
            movie_name = request.GET.get('movie')
            posts =  Movie.objects.filter(name=movie_name)
        elif request.GET.get('popularity'):
            try:
                popularity = int(request.GET.get('popularity'))
                print(popularity , type(popularity))
                posts =  Movie.objects.filter(popularity__gte=popularity)

            except:
                return JsonResponse({"error": "seems popularity is not in integers"})
        else:    
            posts = Movie.objects.all()
        serializer = MovieSerializer(posts, many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def post_movie(request):
    name = []
    movie_data = json.loads(request.body)
    movie_data = movie_data['data']
    duplicate_flag = False
    for data in movie_data:
        name.append(data['name'])    
        genre = data['genre']
        if Movie.objects.filter(name = data['name']):
            duplicate_flag = True
            continue 
        movie_instance =Movie(name= data['name'], popularity=data['99popularity'],score=data['imdb_score'] , director=data['director'])
        movie_instance.save()
        for i in genre:
            Genre(movie_name=movie_instance, genre=i).save()
    if duplicate_flag:
        return Response({'status': 'updated','Note': "some movies were already there if you want to update those we will soon implementing the method for you"})
    return Response({'status': 'Added'})

@api_view(['PUT','DELETE'])
def update_movie(request):
    if request.method =='PUT':
        print(json.loads(request.body))
        movie_data = json.loads(request.body)
        movie_data = movie_data['data']
        for data in movie_data:
            print("data----",data)
            id = data['id']
            Movie.objects.filter(id=id).update(name= data['name'], popularity=data['99popularity'],score=data['imdb_score'] , director=data['director'])
        ### delete the data first from foriegn table
        #TODO: chanhe the below logic
            Genre.objects.filter(id=id).delete()
            for i in data['genre']:
                Genre(movie_name_id=id, genre=i).save()
        return Response({'status': 'updated'})
    if request.method =='DELETE':
        data = json.loads(request.body)
        id = data['id']
        print(id)
        Movie.objects.filter(id=id).delete()
        #TODO: chanhe the below logic
        Genre.objects.filter(id=id).delete()
        return Response({'status': 'deleted'})
