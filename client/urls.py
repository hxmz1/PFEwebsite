from django.urls import path
from . import views

urlpatterns=[
    path('client/<str:id>',views.dashboardclient,name='dashboardclient'),
    path('data',views.mqtt,name='mqtt'),
   
    
]