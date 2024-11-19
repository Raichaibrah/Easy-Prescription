from django.db import models

class Fichier(models.Model):
    titre = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='uploads/')  # ou 'images/' pour des images
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __nom__(self):
        return self.titre
