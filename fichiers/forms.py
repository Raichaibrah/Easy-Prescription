from django import forms
from fichiers.models import Fichier

class FichierForm(forms.ModelForm):
    class Meta:
        model = Fichier
        fields = ['titre', 'fichier']
