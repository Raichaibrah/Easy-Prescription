from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="Âge")
    poids = models.FloatField(null=True, blank=True, verbose_name="Poids (kg)")
    taille = models.FloatField(null=True, blank=True, verbose_name="Taille (cm)")
    email = models.EmailField(null=True, blank=True)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    code_postal= models.CharField(max_length=10)
    pays= models.CharField(max_length=100)
    groupe_sanguin = models.CharField(
        max_length=3, 
        null=True, 
        blank=True, 
        verbose_name="Groupe sanguin",
        choices=[
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Utilisation d'un related_name unique
        blank=True,
        help_text="Les groupes auxquels cet utilisateur appartient.",
        verbose_name="groupes",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Utilisation d'un related_name unique
        blank=True,
        help_text="Autorisations spécifiques pour cet utilisateur.",
        verbose_name="autorisations utilisateur",
    )   