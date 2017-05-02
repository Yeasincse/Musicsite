from django.http import HttpResponse
from django.template import loader

from music.models import Album

def index(request):
    all_album=Album.objects.all()
    template=loader.get_template("music/index.html")
    context={
        'all_album':all_album
    }
    return HttpResponse(template.render(context, request))

def details(request, album_id):
    return HttpResponse("<h1>This is new website : " +str(album_id)+"</h1>")
