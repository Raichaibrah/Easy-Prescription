from django.db import models

class Fichier(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='uploads/', blank=True, null=True)  # Champ temporaire pour garder une copie locale
    drive_url = models.URLField(blank=True, null=True)  # Lien Google Drive

    def __name__(self):
        return self.nom
