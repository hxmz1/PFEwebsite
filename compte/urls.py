from django.urls import path
from . import views

urlpatterns=[
    path('<str:pseudo>',views.inscritclient,name='inscritclient')
    
]
