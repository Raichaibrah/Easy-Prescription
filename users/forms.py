from django import forms
from .models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['age', 'poids', 'taille', 'groupe_sanguin']
        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': 'Âge'}),
            'poids': forms.NumberInput(attrs={'placeholder': 'Poids (kg)'}),
            'taille': forms.NumberInput(attrs={'placeholder': 'Taille (cm)'}),
            'groupe_sanguin': forms.Select(),
        }