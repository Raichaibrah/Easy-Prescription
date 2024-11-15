from django.db import models

# Create your models here.

"""
Pharmacie
nom
adresse
email  

"""

class Pharmacie(models.Model):
    nom = models.CharField(max_length=128)
    adresse = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"