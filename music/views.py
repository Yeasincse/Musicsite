from django.http import HttpResponse

from music.models import Album

def index(request):
    all_album=Album.objects.all()
    html=''
    for album in all_album:
        url='music'+ str(album.id) + '/'
        html +=' <a href= " ' + url + ' " > ' + album.album_title + ' </a> <br> '
    return HttpResponse(html)

def details(request, album_id):
    return HttpResponse("<h1>This is new website : " +str(album_id)+"</h1>")
