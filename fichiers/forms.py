from django import forms
from pharmacies.models import Pharmacie  # Importez le modèle Pharmacie

class OrdonnanceForm(forms.Form):
    fichier = forms.FileField(label="Choisissez un fichier")
    nom_personnalise = forms.CharField(
        label="Nom du fichier (optionnel)", max_length=255, required=False
    )
    commentaire = forms.CharField(
        label="Commentaires (optionnel)", widget=forms.Textarea, required=False
    )
    pharmacie = forms.ModelChoiceField(
        queryset=Pharmacie.objects.all(), 
        label="Choisissez une pharmacie"
    )
