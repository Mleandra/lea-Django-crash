from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Manga ,Mangaka,Reservation,Client

# Create your views here.
def index(request):
    mangas=Manga.objects.filter(disponible=True)
    f_mangas=["<li>{}</li>".format(manga.nom)for manga in mangas]
    message ="""<ul>{}</ul>""".format("".join(f_mangas))
    template =loader.get_template('store/index.html')
    return HttpResponse(template.render(request=request))

def listage(request):
    mangas = Manga.objects.filter(disponible=True)
    f_mangas = ["<li>{}</li>".format(manga.nom) for manga in mangas]
    message = """<ul>{}</ul>""".format("".join(f_mangas))
    return HttpResponse(message)

def detail(request,manga_id):
    manga = Manga.objects.get(pk=manga_id)
    mangakas= "".join([mangaka.nom for mangaka in Manga.mangakas.all()])
    message ="le manga est{}.et l'auteur ou les auteurs sont :{}".format(manga.nom,mangakas)
    return HttpResponse(message)



