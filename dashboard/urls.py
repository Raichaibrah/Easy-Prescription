# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),  # Remplace 'dashboard' par 'index'
    path('pharmacie/<slug:slug>/', views.pharmacie_detail, name='pharmacie_detail'),
]