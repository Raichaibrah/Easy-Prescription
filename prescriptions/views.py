from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from fichiers.models import Ordonnance
from fichiers.storage import GoogleDriveStorage

@login_required
def historique_ordonnances(request):
    # Récupère toutes les ordonnances soumises par l'utilisateur
    ordonnances = Ordonnance.objects.filter(user=request.user) #pylint: disable=no-member
    return render(request, 'prescriptions/historique_ordonnances.html', {'ordonnances': ordonnances})

@login_required
def soumettre_ordonnance(request):
    return render(request, 'fichiers/televerser.html')

@login_required
def supprimer_ordonnance(request, id):
    # Récupérer l'ordonnance à supprimer
    ordonnance = get_object_or_404(Ordonnance, id=id)
    
    # Vérifier si l'utilisateur authentifié est bien celui qui a soumis l'ordonnance
    if ordonnance.user != request.user:
        messages.error(request, "Vous ne pouvez pas supprimer cette ordonnance.")
        return redirect('historique_ordonnances')

    # Supprime l'ordonnance dans le google drive 
    storage = GoogleDriveStorage.get_instance()
    file_id=storage.get_file_id_by_name(id)
    storage.delete_file(file_id)
    
    # Supprimer l'ordonnance
    ordonnance.delete()
    
    # Ajouter un message de succès et rediriger vers l'historique des ordonnances
    messages.success(request, "L'ordonnance a été supprimée avec succès.")
    return redirect('historique_ordonnances')
