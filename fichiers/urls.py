from django.urls import path
import fichiers.views


app_name = 'fichiers'

urlpatterns = [
    path('televerser/', fichiers.views.televerser_ordonnance, name='televerser_ordonnance'),
]
