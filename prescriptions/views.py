from django.shortcuts import render

# Create your views here.
from fichiers.models import Ordonnance
from django.contrib.auth.decorators import login_required

@login_required
def historique_ordonnances(request):
    # Récupère toutes les ordonnances soumises par l'utilisateur
    ordonnances = Ordonnance.objects.filter(user=request.user) #pylint: disable=no-member
    return render(request, 'prescriptions/historique_ordonnances.html', {'ordonnances': ordonnances})
@login_required
def soumettre_ordonnance(request):
    return render(request, 'fichiers/televerser.html')