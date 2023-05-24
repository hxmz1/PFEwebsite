from django.urls import path
from . import views

urlpatterns=[
    path('/<int:id>',views.dashboardclient,name='dashboardclient'),
    path('data/<int:id>',views.mqtt,name='mqtt'),
    path('mqtt_two/<int:id>', views.mqtt_two, name='mqtt_two'),
   
    
]