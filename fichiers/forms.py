from django import forms

class FichierForm(forms.Form):
    fichier = forms.FileField()
