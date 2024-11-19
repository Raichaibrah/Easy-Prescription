from django import forms
from .models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['age', 'poids', 'taille', 'groupe_sanguin', 'tel', 'adresse', 'ville', 'code_postal', 'pays']
        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': 'Âge'}),
            'poids': forms.NumberInput(attrs={'placeholder': 'Poids (kg)'}),
            'taille': forms.NumberInput(attrs={'placeholder': 'Taille (cm)'}),
            'groupe_sanguin': forms.Select(),
            'tel' : forms.NumberInput(attrs={'placeholder': 'Numéro de téléphone'}),
            'adresse': forms.TextInput(attrs={'placeholder': 'Adresse'}),
            'ville': forms.TextInput(attrs={'placeholder': 'Ville'}),
            'code_postal': forms.TextInput(attrs={'placeholder': 'Code postal'}),
            'pays': forms.TextInput(attrs={'placeholder': 'Pays'}),

        }


