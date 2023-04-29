from django.urls import path
from . import views

urlpatterns=[
    path('',views.inscritsuperviseur,name='inscritsuper'),
    path('<str:variable>/map/<str:pseudo>',views.maps,name='map')
]
