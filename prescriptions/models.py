from django.db import models

# Create your models here.
# ordonnances/models.py
from pharmacies.models import Pharmacie  # Assurez-vous que l'importation est correcte
from django.conf import settings
class Ordonnance(models.Model):
    # Statut de l'ordonnance : en attente, traitée, etc.
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('traitee', 'Traité'),
        ('annulee', 'Annulée'),
    ]
    
    # L'utilisateur qui soumet l'ordonnance (Patient)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # La pharmacie à laquelle l'ordonnance est envoyée
    pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE)
    
    # Date de soumission de l'ordonnance
    date_creation = models.DateTimeField(auto_now_add=True)
    
    # Statut de l'ordonnance
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    
    # Un champ pour l'image de l'ordonnance (fichier téléchargé)
    ordonnance_image = models.ImageField(upload_to='ordonnances/', blank=True, null=True)

    def __str__(self):
        return f"Ordonnance {self.id} - {self.get_statut_display()}" #pylint: disable=no-member
