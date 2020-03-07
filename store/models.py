from django.db import models

# Create your models here.
class Mangaka(models.Model):

    nom = models.CharField(max_length = 100)

    def __str__(self):
        return self.nom

class Manga (models.Model):
    nom = models.CharField(max_length = 100)
    reference = models.IntegerField(null=True)
    creation = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    mignature = models.URLField()
    mangakas = models.ManyToManyField(Mangaka ,related_name='mangas', blank=True)

    def __str__(self):
        return self.nom



class Client(models.Model):

    nom = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.nom


class Reservation(models.Model):

    creation = models.DateField(auto_now_add=True)
    livre = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    manga = models.OneToOneField(Manga ,on_delete=models.CASCADE)

    def __str__(self):
        return self.client.nom