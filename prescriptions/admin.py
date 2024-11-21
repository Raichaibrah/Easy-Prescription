from django.contrib import admin

# Register your models here.
from django.contrib import admin
from fichiers.models import Ordonnance

class OrdonnanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pharmacie', 'date_creation', 'statut')
    list_filter = ('statut', 'pharmacie')
    search_fields = ('user__username', 'pharmacie__name')

admin.site.register(Ordonnance, OrdonnanceAdmin)