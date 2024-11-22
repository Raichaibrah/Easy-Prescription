from django.urls import path
from . import views

app_name = 'prescriptions'

urlpatterns = [
    path('historique/', views.historique_ordonnances, name='historique_ordonnances'),
    path('ordonnance/<int:id>/supprimer/', views.supprimer_ordonnance, name='supprimer_ordonnance'),
    path('soumettre/', views.soumettre_ordonnance, name='soumettre_ordonnance'),
]