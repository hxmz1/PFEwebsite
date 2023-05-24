from django.urls import path
from . import views

urlpatterns=[
    path(' ',views.connexion,name='connexion'),
    
    path(' <str:pseudo>',views.dashboardsuperviseur,name='dashboardsuperviseur'),
    path('connexionclient',views.connxionClient,name='connexionclient'),
    path('connexionsuperviseur',views.connexionSuperviseur,name='connexionsuperviseur'),


]