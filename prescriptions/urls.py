from django.urls import path
from . import views


urlpatterns = [
    path('historique/', views.historique_ordonnances, name='historique_ordonnances'),
    path('ordonnance/<int:id>/supprimer/', views.supprimer_ordonnance, name='supprimer_ordonnance'),
]