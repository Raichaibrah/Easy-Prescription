from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from pharmacies.models import Pharmacie


# Create your views here.

def index(request):
    pharmacie = Pharmacie.objects.all()
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
        pharmacies = Pharmacie.objects.filter(ville__icontains=search_city)
        print(f"Pharmacies trouvées pour la ville '{search_city}': {pharmacies}")
    else:
        pharmacies = Pharmacie.objects.all()  # Si pas de ville, on récupère toutes les pharmacies

    # Passer les pharmacies filtrées et la ville recherchée dans le template
    return render(request, 'dashboard/index.html', {'pharmacies': pharmacies, 'search_city': search_city})