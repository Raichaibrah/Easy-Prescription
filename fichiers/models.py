from django.db import models

class Fichier(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='uploads/', blank=True, null=True)
    drive_url = models.URLField(blank=True, null=True)
    commentaires = models.TextField(blank=True, null=True)  # Stocker les commentaires optionnellement

    def __name__(self):
        return self.nom
