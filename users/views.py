from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate


Utilisateur = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
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