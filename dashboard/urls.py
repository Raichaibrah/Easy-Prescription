# dashboard/urls.py
from django.urls import path
from . import views
app_name = 'dashboard'  

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('', views.home, name='home'),  # Page d'accueil
    path('index/', views.index, name='index'),  # Liste des pharmacies
    path('dashboard/', views.dashboard, name='dashboard'),  # Recherche
    path('page-pharmacie/', views.page_pharmacie, name='page_pharmacie'),
    
    path('<slug:slug>/', views.pharmacie_detail, name='pharmacie_detail'),  # Détails d'une pharmacie  
]