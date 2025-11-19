from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from imdb_api.models import WatchList
from .serializer import WatchlistSerializer,StreamPlatformSerializer


# Create your views here.

def movie_list(request):
    movie_list = WatchList.objects.all()
    serialized = WatchlistSerializer(movie_list,many=True)
    return JsonResponse(serialized.data,safe = False)


def movie_detail(request,pk):
    movie = WatchList.objects.get(pk=pk)
    serialized = WatchlistSerializer(movie)


    return JsonResponse(serialized.data)

