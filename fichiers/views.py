from django.shortcuts import render, redirect
from fichiers.forms import FichierForm
from fichiers.models import Fichier
import os
from fichiers.storage import GoogleDriveStorage  # Import de la classe GoogleDriveStorage (voir plus bas)
from django.contrib.auth.decorators import login_required


@login_required
def televerser_fichier(request):
    if request.method == 'POST' and request.FILES['fichier']:
        form = FichierForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.cleaned_data['fichier']
            nom_personnalise = form.cleaned_data['nom_personnalise'] or fichier.name
            commentaires = form.cleaned_data['commentaires']

            # Sauvegarde temporaire du fichier localement
            fichier_obj = Fichier(nom=nom_personnalise, fichier=fichier)
            fichier_obj.save()

            # Chemin temporaire pour stocker le fichier
            file_path = fichier_obj.fichier.path  # pylint: disable=no-member
            custom_file_path = os.path.join("media/uploads", nom_personnalise)
            os.rename(file_path, custom_file_path)

            # Création du fichier de commentaires localement
            if commentaires:
                comments_file_path = f"{custom_file_path}_comments.txt"
                with open(comments_file_path, "w", encoding="utf-8") as comments_file:
                    comments_file.write(commentaires)

                # Téléversement du fichier de commentaires sur Google Drive
                storage = GoogleDriveStorage()
                storage.upload_file(comments_file_path, f"{nom_personnalise}_comments.txt")

            # Téléversement du fichier principal sur Google Drive
            storage = GoogleDriveStorage()
            drive_url = storage.upload_file(custom_file_path, nom_personnalise)

            # Met à jour l'URL du fichier dans la base de données
            fichier_obj.drive_url = drive_url
            fichier_obj.save()

            return redirect('fichiers:televerser_fichier')  # Redirection après succès

    else:
        form = FichierForm()

    return render(request, 'fichiers/televerser.html', {'form': form})

