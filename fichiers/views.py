from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fichiers.forms import OrdonnanceForm
from fichiers.models import Ordonnance
from fichiers.storage import GoogleDriveStorage  
import os

@login_required
def televerser_ordonnance(request):
    if request.method == 'POST':
        form = OrdonnanceForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.cleaned_data['fichier']
            nom_personnalise = form.cleaned_data['nom_personnalise'] or fichier.name
            commentaire = form.cleaned_data['commentaire']
            pharmacie = form.cleaned_data['pharmacie']

            # Création de l'objet Ordonnance avec l'URL publique
            ordonnance = Ordonnance.objects.create( #pylint: disable=no-member
                user=request.user,
                pharmacie=pharmacie,
                commentaire=commentaire,
                drive_file_url='None', #Pas d'URL à la création de l'objet, car le fichier n'est pas encore en ligne
                nom_fichier=nom_personnalise
            )
            # Téléversement sur Google Drive
            storage = GoogleDriveStorage()
            file_path = f"media/temp/{fichier.name}"
            with open(file_path, 'wb+') as destination:
                for chunk in fichier.chunks():
                    destination.write(chunk)
                    
            # Appel de la méthode pour uploader et obtenir l'URL publique
            drive_url = storage.upload_file(file_path, ordonnance.id)
            
            #Modification de l'URL a posteriori 
            ordonnance.drive_file_url = drive_url
            
            ordonnance.save()
            
            print("ordonnance :",ordonnance)
            
            # Nettoyage du fichier temporaire local
            os.remove(file_path)

            return redirect('historique_ordonnances')  # Redirection après succès
    else:
        form = OrdonnanceForm()

    return render(request, 'fichiers/televerser_ordonnance.html', {'form': form})
