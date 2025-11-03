from urllib.request import Request

from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.


def movie_list(request: Request):
    movies = Movie.objects.all()
    print(movies.values())
    response = {
        # we need to convert query set return ed by django into list
        "list": list(movies.values())
    }
    return JsonResponse(response)
