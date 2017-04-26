from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is new website</h1>")
def details(request, album_id):
    return HttpResponse("<h1>This is new website" +str(album_id)+"</h1>")
