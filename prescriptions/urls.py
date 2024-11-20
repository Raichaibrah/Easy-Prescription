from django.urls import path
from . import views

urlpatterns = [
    path('historique/', views.historique_ordonnances, name='historique_ordonnances'),
   path('soumettre/', views.soumettre_ordonnance, name='soumettre_ordonnance'),
]