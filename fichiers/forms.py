from django import forms

class FichierForm(forms.Form):
    fichier = forms.FileField(label="Fichier")
    nom_personnalise = forms.CharField(
        label="Nom du fichier (optionnel)", max_length=255, required=False
    )
    commentaires = forms.CharField(
        label="Commentaires (optionnel)", widget=forms.Textarea, required=False
    )
