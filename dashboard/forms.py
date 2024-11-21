from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Votre adresse e-mail", max_length=254)
    objet = forms.ChoiceField(
        choices=[
            ('pharmacie', 'Devenir pharmacie partenaire'),
            ('renseignement', 'Demande de renseignement'),
            ('autre', 'Autre'),
        ],
        label="Objet"
    )
    message = forms.CharField(widget=forms.Textarea, label="Votre message")
