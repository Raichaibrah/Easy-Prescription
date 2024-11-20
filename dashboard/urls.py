# dashboard/urls.py
from django.urls import path
from . import views
app_name = 'dashboard'  

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('index/', views.index, name='index'),  # Liste des pharmacies
    path('dashboard/', views.dashboard, name='dashboard'),  # Recherche
    path('<slug:slug>/', views.pharmacie_detail, name='pharmacie_detail'),  # Détails d'une pharmacie
]