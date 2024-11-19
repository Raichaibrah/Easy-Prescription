from django.urls import path
import fichiers.views


app_name = 'fichiers'

urlpatterns = [
    path('televerser/', fichiers.views.televerser_fichier, name='televerser_fichier'),
]
