from django.db import models
from django.contrib.gis.db import models

class Superviseur(models.Model):
    id = models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    superviseur_id=models.CharField(max_length=100, null=True, unique=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    NB_GSM = models.CharField(max_length=100, null=True)
    identifiant = models.CharField(max_length=100, null=True)
    e_mail = models.EmailField(max_length=100, null=True)
    superviseur = models.ForeignKey(Superviseur, on_delete=models.CASCADE, null=True, related_name='%(class)s_related')
    """created_at = models.DateTimeField(auto_now_add=True)"""
    

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    




class nodes(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
    Position = models.PointField(null=True)
    Latitude = models.CharField(max_length=50, null=True, blank=True)
    Longitude = models.CharField(max_length=50, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name='%(class)s_related')
    
   
    
    def __str__(self):
        return "Node " + str(self.Name)

    class Meta:
        verbose_name_plural = "Nodes"
        verbose_name = "Node"    



class Data(models.Model):
    IdData = models.AutoField(primary_key=True)
    temperature = models.BigIntegerField()
    humidity = models.BigIntegerField()
    
    nodes = models.ForeignKey(nodes, on_delete=models.CASCADE, null=True, related_name='datas')
    
    
    
    def __str__(self):
        return f' node : {self.nodes},Temperature: {self.temperature}, Humidity: {self.humidity}'
