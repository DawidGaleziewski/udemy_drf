from urllib.request import Request

from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.

# doing json response by hand
def movie_list(request: Request):
    movies = Movie.objects.all()
    # we serialize the data from complex model objects into Json
    response = {
        # we need to convert query set return ed by django into list
        "list": list(movies.values())
    }
    return JsonResponse(response)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    response= {
        "movie": {
            "name": movie.name,
            "desc": movie.description
        }
    }
    return JsonResponse(response)
