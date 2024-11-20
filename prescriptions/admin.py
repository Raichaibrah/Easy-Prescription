from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ordonnance

class OrdonnanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pharmacie', 'date_creation', 'statut', 'ordonnance_image')
    list_filter = ('statut', 'pharmacie')
    search_fields = ('user__username', 'pharmacie__name')

admin.site.register(Ordonnance, OrdonnanceAdmin)