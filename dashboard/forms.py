from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        label="Votre email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre email',
        })
    )
    objet = forms.ChoiceField(
        label="Objet",
        choices=[
            ('partenaire', 'Devenir pharmacie partenaire'),
            ('info', 'Demande d’information'),
            ('probleme', 'Problème patient'),
            ('autre', 'Autre')
        ],
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    message = forms.CharField(
        label="Votre message",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre message ici',
            'rows': 5,
        })
    )
