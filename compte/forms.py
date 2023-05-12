from django import forms
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from .models import *

class client(forms.Form):
    nom = forms.CharField(required=True, max_length=Client._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': "nom", 'name': "nom", 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px", 'placeholder': 'Nom'}))
    prenom = forms.CharField(required=True, max_length=Client._meta.get_field(
        'prenom').max_length, widget=forms.TextInput(attrs={'id': 'prenom', 'name': 'prenom', 'placeholder': 'Prénom', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    telephone = forms.CharField(required=True, max_length=Client._meta.get_field(
        'NB_GSM').max_length, widget=forms.TextInput(attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'placeholder': 'Téléphone', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    id = forms.CharField(required=True, max_length=Client._meta.get_field(
        'identifiant').max_length, widget=forms.TextInput(attrs={'id': 'identifiant', 'name': 'identifiant', 'placeholder': 'ID', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    email = forms.EmailField(max_length=Client._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email', 'placeholder': 'E-Mail', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'name': 'password', 'placeholder': 'Mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'name': 'password1', 'placeholder': 'Re-saisir le mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))

    def is_valid(self):
        nom = self.data['nom']
        if any(char.isdigit() for char in nom):
            self.add_error("nom", "Nom est incorrect!")
        prenom = self.data['prenom']
        if any(char.isdigit() for char in prenom):
            self.add_error("prenom", "Prenom est incorrect!")
        id = self.data['id']
        if Client.objects.filter(identifiant=id).exists():
            self.add_error("identifiant", "identifiant déja existant!")
        email = self.data['email']
        if Client.objects.filter(e_mail=email).exists():
            self.add_error("email", "email déja existant!")
        telephone = self.data['telephone']
        if not telephone.isdigit():
            self.add_error("telephone", "Téléphone est incorrect!")
        mot_de_passe = self.data['mot_de_passe']
        if len(mot_de_passe) < 8:
            self.add_error(
                "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
        confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
        if confirmation_mot_de_passe != mot_de_passe:
            self.add_error("confirmation_mot_de_passe",
                           "Les mots de passe ne correspondent pas.")
        value = super(client, self).is_valid()
        return value

    def enregistrer(self, superviseur):
        nom = self.cleaned_data['nom']
        prenom = self.cleaned_data['prenom']
        email = self.cleaned_data['email']
        id = self.cleaned_data['id']
        telephone = self.cleaned_data['telephone']
        confirmation_mot_de_passe = self.cleaned_data['confirmation_mot_de_passe']
        clientdata = Client(nom=nom, prenom=prenom, identifiant=id,
                          NB_GSM=telephone, e_mail=email, superviseur = superviseur)
        clientdata.save()

        
        clientdata = User.objects.create_user(
            id, email, confirmation_mot_de_passe)
        clientdata.save()


class superviseur(forms.Form):
    nom = forms.CharField(required=True, max_length=Superviseur._meta.get_field(
        'nom').max_length, widget=forms.TextInput(attrs={'id': "nom", 'name': "nom", 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px", 'placeholder': 'Nom'}))
    prenom = forms.CharField(required=True, max_length=Superviseur._meta.get_field(
        'prenom').max_length, widget=forms.TextInput(attrs={'id': 'prenom', 'name': 'prenom', 'placeholder': 'Prénom', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    telephone = forms.CharField(required=True, max_length=Superviseur._meta.get_field(
        'NB_GSM').max_length, widget=forms.TextInput(attrs={'id': 'NB_GSM', 'name': 'NB_GSM', 'placeholder': 'Téléphone', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    pseudo = forms.CharField(required=True, max_length=Superviseur._meta.get_field(
        'pseudo').max_length, widget=forms.TextInput(attrs={'id': 'pseudo', 'name': 'pseudo', 'placeholder': 'Pseudo', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    email = forms.EmailField(max_length=Superviseur._meta.get_field(
        'e_mail').max_length, required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email', 'placeholder': 'E-Mail', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password', 'name': 'password', 'placeholder': 'Mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))
    confirmation_mot_de_passe = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'id': 'password1', 'name': 'password1', 'placeholder': 'Re-saisir le mot de passe', 'class': "form-control shadow-lg p-6 mb-6 rounded", 'style': "font-size: 20px"}))

    def is_valid(self):
        nom = self.data['nom']
        if any(char.isdigit() for char in nom):
            self.add_error("nom", "Nom est incorrect!")
        prenom = self.data['prenom']
        if any(char.isdigit() for char in prenom):
            self.add_error("prenom", "Prenom est incorrect!")
        pseudo = self.data['pseudo']
        if Superviseur.objects.filter(pseudo=pseudo).exists():
            self.add_error("pseudo", "pseudo déja existant!")
        email = self.data['email']
        if Superviseur.objects.filter(e_mail=email).exists():
            self.add_error("email", "email déja existant!")
        telephone = self.data['telephone']
        if not telephone.isdigit():
            self.add_error("telephone", "Téléphone est incorrect!")
        mot_de_passe = self.data['mot_de_passe']
        if len(mot_de_passe) < 8:
            self.add_error(
                "mot_de_passe", "Le mot de passe doit contenir au moins 8 caractères.")
        confirmation_mot_de_passe = self.data['confirmation_mot_de_passe']
        if confirmation_mot_de_passe != mot_de_passe:
            self.add_error("confirmation_mot_de_passe",
                           "Les mots de passe ne correspondent pas.")
        value = super(superviseur, self).is_valid()
        return value

    def enregistrer(self):
        nom = self.cleaned_data['nom']
        prenom = self.cleaned_data['prenom']
        email = self.cleaned_data['email']
        pseudo = self.cleaned_data['pseudo']
        telephone = self.cleaned_data['telephone']
        mot_de_passe = self.cleaned_data['mot_de_passe']
        data = Superviseur(nom=nom, prenom=prenom, NB_GSM=telephone,
                       pseudo=pseudo, e_mail=email)
        data.save()
        data = User.objects.create_user(
            pseudo, email, mot_de_passe)
        data.save()


class position(forms.Form):
    latitude = forms.FloatField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'lat', 'name': 'lat'}))
    longitude = forms.FloatField(required=False, widget=forms.HiddenInput(
        attrs={'id': 'lng', 'name': 'lng'}))

    def is_valid(self):
        lat = self.data['latitude']
        lng = self.data['longitude']
        if lat == '' or lng == '':
            self.add_error("latitude", "choisit votre position")
        value = super(position, self).is_valid()
        return value

    def enregistrer_noeud(self, pseudo):
        lat = self.cleaned_data['latitude']
        lng = self.cleaned_data['longitude']
        point = Point(x=float(lng), y=float(lat))
        data = Client.objects.get(pseudo=pseudo)
        if data:
            data.position = point
            data.save()
