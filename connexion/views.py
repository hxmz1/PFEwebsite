
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
# Create your views here.
def connexion(request):
    return render(request, "loginas.html")

def connxionClient(request):
    if request.method == 'POST':
        formulaire = LoginasClient(request.POST)
        if formulaire.is_valid():
            id = formulaire.cleaned_data['identifiant']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=id,
                                password=mot_de_passe)
            if data is not None:
                login(request,data)
                return redirect('home')
        # We pass the form to the template even if it is not valid
        return render(request, 'loginclient.html', {'formclient': formulaire})
    # We pass the form to the template for GET requests
    return render(request, 'loginclient.html', {'formclient': LoginasClient()})







"""superviseur feedjk"""

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginasSuperviseur


def connexionSuperviseur(request):
    if request.method == 'POST':
        formulaire = LoginasSuperviseur(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            superviseur = authenticate(username=pseudo, password=mot_de_passe)
            if superviseur is not None:
                login(request, superviseur)
                return render(request, 'pagesuperviseur.html', {'form': formulaire})
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Invalid login form.')
    else:
        formulaire = LoginasSuperviseur()
    return render(request, 'loginsuperviseur.html', {'form': formulaire})

