from django.db import models
from django.conf import settings
from pharmacies.models import Pharmacie  

class Ordonnance(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('traitee', 'Traité'),
        ('annulee', 'Annulée'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    commentaire = models.TextField(blank=True, null=True)  # Commentaire fourni par l'utilisateur
    drive_file_url = models.URLField(blank=True, null=True)  # URL du fichier téléversé
    nom_fichier=models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Ordonnance {self.id} - {self.get_statut_display()}"
