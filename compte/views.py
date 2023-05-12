from django.shortcuts import render, redirect
from .forms import *
from .models import Client, Superviseur
from superviseur.views import *


# Create your views here.


"""def inscritsuperviseur(request):
    if request.method == 'POST':
        formulaire = superviseur(request.POST)
        if formulaire.is_valid():
            formulaire.enregistrer()
            return redirect('connexionsuperviseur')
        return render(request, 'signup.html', {'form': formulaire})
    return render(request, 'signup.html', {'form': superviseur()})"""

def inscritclient(request, pseudo):
    
    if request.method == 'POST':
        formul = client(request.POST)
        if formul.is_valid():
            superviseur = Superviseur.objects.get(pseudo=pseudo)
            
            formul.enregistrer(superviseur)
            client_id = formul.cleaned_data['id']
            print(client_id)
            
            return redirect('add_node', pseudo=pseudo , client_id=client_id)
        return render(request, 'signup.html', {'form': formul})
    return render(request, 'signup.html', {'form': client()})


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

