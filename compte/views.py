from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.


def inscritsuperviseur(request):
    if request.method == 'POST':
        formulaire = superviseur(request.POST)
        if formulaire.is_valid():
            formulaire.enregistrer()
            return redirect('connexionsuperviseur')
        return render(request, 'signup.html', {'form': formulaire})
    return render(request, 'signup.html', {'form': superviseur()})

"""def inscritclient(request):
    if request.method == 'POST':
        formulaire = client(request.POST)
        if formulaire.is_valid():
            formulaire.enregistrer()
            return redirect('login')
        return render(request, 'page1/inscrire.html', {'form': formulaire})
    return render(request, 'page1/inscrire.html', {'form': superviseur()})"""


"""def inscritclient(request, superviseur_id):
    superviseur = Superviseur.objects.get(id=superviseur_id)

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.superviseur = superviseur
            client.save()
            return redirect('client_detail', client.id)
    else:
        form = ClientForm()

    context = {'form': form, 'superviseur': superviseur}
    return render(request, 'create_client.html', context)"""


def maps(request, variable, pseudo):
    if request.method == 'POST':
        formulaire = position(request.POST)
        if formulaire.is_valid():
            if variable == 'superviseur':
                formulaire.enregistrer_noeud()
                return redirect('map', variable, pseudo)
            
        return render(request, 'pagesuperviseur.html', {'form': formulaire})
    return render(request, 'pagesuperviseur.html', {'form': position()})

