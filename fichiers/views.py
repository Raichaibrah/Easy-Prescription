from django.shortcuts import render, redirect
from fichiers.forms import FichierForm
from fichiers.models import Fichier
from fichiers.storage import GoogleDriveStorage  # Import de la classe GoogleDriveStorage (voir plus bas)

def televerser_fichier(request):
    if request.method == 'POST' and request.FILES['fichier']:
        form = FichierForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.cleaned_data['fichier']

            # Sauvegarde temporaire du fichier localement (avant de le téléverser sur Google Drive)
            fichier_obj = Fichier(nom=fichier.name, fichier=fichier)
            fichier_obj.save()

            # Téléversement sur Google Drive
            storage = GoogleDriveStorage()
            file_path = fichier_obj.fichier.path  # Récupère le chemin du fichier temporaire #pylint: disable=no-member
            drive_url = storage.upload_file(file_path, fichier_obj.fichier.name)

            # Met à jour l'URL du fichier dans la base de données
            fichier_obj.drive_url = drive_url
            fichier_obj.save()

            return redirect('fichiers:televerser_fichier')  # Redirection après téléversement réussi

    else:
        form = FichierForm()

    return render(request, 'fichiers/televerser.html', {'form': form})

