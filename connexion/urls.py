from django.urls import path
from . import views

urlpatterns=[
    path('connexion/',views.connexion,name='connexion'),
    
    path('connexionsuperviseur/<str:pseudo>',views.dashboardsuperviseur,name='dashboardsuperviseur'),
    path('connexionclient/',views.connxionClient,name='connexionclient'),
    path('connexionsuperviseur/',views.connexionSuperviseur,name='connexionsuperviseur'),


]