from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('postion/<str:pseudo>/<str:client_id>',views.add_node,name='add_node'),
    path('allnodes',views.all_nodes,name='allnodes')
    
]