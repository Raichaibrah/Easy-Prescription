from django.shortcuts import render, redirect
from fichiers.forms import FichierForm
from pharmacies.fonctions_utiles import fonction_1, fonction_2 

def televerser_fichier(request):
    if request.method == 'POST':
        form = FichierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fichiers:televerser_fichier')
    else:
        form = FichierForm()
    
    return render(request, 'fichiers/televerser.html', {'form': form})

