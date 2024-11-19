from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages  # Pour afficher des messages d'erreur
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm


Utilisateur = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")  # Nouveau champ

        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'users/signup.html')

        utilisateur = Utilisateur.objects.create_user(username=username, password=password)
        login(request, utilisateur)
        return redirect('index')

    return render(request, 'users/signup.html')


def login_user(request):
    if request.method == "POST":
        #Connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")

        utilisateur = authenticate(username=username, password=password)
        if utilisateur:
            login(request, utilisateur)
            return redirect('index')

    return render(request, 'users/login.html')



def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def profil(request):
    utilisateur = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour avec succès.")
            return redirect('profil')
    else:
        form = ProfileForm(instance=utilisateur)

    return render(request, 'users/profil.html', {'form': form})

