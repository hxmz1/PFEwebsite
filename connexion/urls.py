from django.urls import path
from . import views

urlpatterns=[
    path('connexion/',views.connexion,name='connexion'),
    path('connexionclient/',views.connxionClient,name='connexionclient'),
    path('connexionsuperviseur/',views.connexionSuperviseur,name='connexionsuperviseur'),


]