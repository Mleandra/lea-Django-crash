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
    context ={'mangas':mangas}
    return HttpResponse(template.render(context ,request=request))

def listage(request):
    mangas = Manga.objects.filter(disponible=True)
    f_mangas = ["<li>{}</li>".format(manga.nom) for manga in mangas]
    message = """<ul>{}</ul>""".format("".join(f_mangas))
    context={'mangas': mangas}
    return HttpResponse(context)

def detail(request,manga_id):
    manga = Manga.objects.get(pk=manga_id)
    mangakas= "".join([mangaka.nom for mangaka in manga.mangakas.all()])
    message ="le manga est{}.et l'auteur ou les auteurs sont :{}".format(manga.nom,mangakas)
    context ={
        'manga_nom': manga.nom,
        'mangaka_nom': mangakas,
        'manga_id': manga.id,
        'image': manga.mignature
    }

    return HttpResponse(context)

def recherche(request):
    query = request.GET.get('query')
    if not query:
        mangas = Manga.objects.all()
        message ="aucun resultat"
    else:
        mangas = Manga.objects.filter(nom__icontains=query)

        if not mangas.exists():
            mangas = Manga.objects.filter(mangakas__nom__icontains=query)
        if not mangas.exists():
            message = 'Aucun resultat disponible'
        else:
            mangas=["<li>{}</li>".format(manga.nom )for manga in mangas]
            message = """resultat:
            <ul>
            {}
            </ul>""".format("</li><li>".join(mangas))

    return HttpResponse(message)



