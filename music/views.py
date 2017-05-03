from django.http import HttpResponse
from django.shortcuts import render

from music.models import Album

def index(request):
    all_album=Album.objects.all()
    context={'all_album':all_album
    }
    return render(request, 'music/index.html', context)

def details(request, album_id):
    return HttpResponse("<h1>This is new website : " +str(album_id)+"</h1>")
