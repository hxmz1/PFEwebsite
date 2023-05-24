
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from compte.models import *
# Create your views here.
def connexion(request):
    return render(request, "loginas.html")

def connxionClient(request):
    if request.method == 'POST':
        formulaire = LoginasClient(request.POST)
        if formulaire.is_valid(request):
            psedo = formulaire.cleaned_data['identifiant']
           
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=psedo,
                                password=mot_de_passe)
            if data is not None:
                client= Client.objects.get(identifiant=psedo)
                id= client.id
                print(id)
                login(request,data)

            return redirect('dashboardclient',id=id)
        # We pass the form to the template even if it is not valid
        return render(request, 'loginclient.html', {'formloginclient': formulaire})
    # We pass the form to the template for GET requests
    return render(request, 'loginclient.html', {'formloginclient': LoginasClient()})







"""superviseur feedjk"""

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginasSuperviseur
def dashboardsuperviseur(request, pseudo):
    superviseur= Superviseur.objects.get(pseudo=pseudo)
    Name=superviseur.nom
    return render (request, 'dashboardsuperviseur.html', {'pseudo': pseudo, 'nom':Name})
def connexionSuperviseur(request):
    if request.method == 'POST':
        formulaire = LoginasSuperviseur(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            superviseur = authenticate(username=pseudo, password=mot_de_passe)
            if superviseur is not None:
                login(request, superviseur)
                print(pseudo)
                return redirect('dashboardsuperviseur',  pseudo=pseudo)
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Invalid login form.')
    else:
        formulaire = LoginasSuperviseur()
    return render(request, 'loginsuperviseur.html', {'form': formulaire})

