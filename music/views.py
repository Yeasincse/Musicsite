from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import render

from music.models import Album

def index(request):
    all_album=Album.objects.all()
    return render(request, 'music/index.html', { 'all_album':all_album })

#def details(request, album_id):
    #return HttpResponse("<h1>This is new website : " +str(album_id)+"</h1>")

def details(request, album_id):
    try:
      album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("The Album does'not exist")
    return render(request, 'music/detail.html', { 'album': album })



