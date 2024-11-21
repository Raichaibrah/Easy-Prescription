from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from pharmacies.models import Pharmacie

from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def index(request):
    pharmacie = Pharmacie.objects.all() #pylint: disable=no-member
    return render(request, 'dashboard/index.html', context = {"pharmacies" : pharmacie})

def pharmacie_detail(request, slug):
    pharmacie = get_object_or_404(Pharmacie, slug=slug)
    print("pharmacie : ",pharmacie.thumbnail)
    return render(request, 'dashboard/detail.html', context={"pharmacie": pharmacie})

def dashboard(request):
    print("Vue 'dashboard' exécutée")
    search_city = request.GET.get('search_city', '')  # Récupérer la ville depuis la barre de recherche

    # Affichage du contenu de la ville recherchée pour vérifier que c'est bien récupéré
    print(f"Recherche effectuée pour la ville : {search_city}")

    # Si une ville est saisie, on filtre les pharmacies par ville
    if search_city:
        # Vérification du filtrage
        pharmacies = Pharmacie.objects.filter(ville__icontains=search_city) #pylint: disable=no-member
        print(f"Pharmacies trouvées pour la ville '{search_city}': {pharmacies}")
    else:
        pharmacies = Pharmacie.objects.all()  # Si pas de ville, on récupère toutes les pharmacies #pylint: disable=no-member

    # Passer les pharmacies filtrées et la ville recherchée dans le template
    return render(request, 'dashboard/index.html', {'pharmacies': pharmacies, 'search_city': search_city})

def home(request):
    return render(request, 'dashboard/home.html')

def page_pharmacie(request):
    # Vous pouvez ajouter des données à rendre ici, comme des informations sur les pharmacies
    context = {
        'title': 'Page Pharmacie',
        'message': 'Bienvenue sur la page des pharmacies!',
    }
    return render(request, 'dashboard/page_pharmacie.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            objet = form.cleaned_data['objet']
            message = form.cleaned_data['message']

            # Construire le sujet et le corps du mail
            subject = f"Contact - {dict(form.fields['objet'].choices)[objet]}"
            body = f"Message de : {email}\n\n{message}"

            # Envoi du mail
            send_mail(
                subject,
                body,
                'votre-adresse-email@votre-domaine.com',  # L'adresse de l'expéditeur
                ['easyprescription23@gmail.com'],  # Adresse de réception
            )

            # Message de succès
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('dashboard:contact')  # Redirection vers la même page après l'envoi
    else:
        form = ContactForm()

    return render(request, 'dashboard/contact.html', {'form': form})