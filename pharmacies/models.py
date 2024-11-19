from django.db import models
from django.urls import reverse

# Create your models here.

"""
Pharmacie
nom
adresse
email  

"""

class Pharmacie(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    adresse = models.CharField(max_length=256)
    ville = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    thumbnail = models.ImageField(upload_to= "p_pharmacies", blank= True, null= True)
    description = models.CharField(max_length=3000)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("pharmacie", kwargs={"slug": self.slug})
    