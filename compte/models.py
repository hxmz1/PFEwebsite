from django.db import models
from django.contrib.gis.db import models

class Superviseur(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Client(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    identifiant=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    position=models.PointField(null=True)
    superviseur = models.ForeignKey(Superviseur, on_delete=models.CASCADE, related_name='clients')
    "date de l'incription + date de l'ajout de chaque noeud "

    def __str__(self):
        return f"{self.prenom} {self.nom}"    
