from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
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