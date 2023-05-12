from django.shortcuts import render, redirect
from .models import *
from django.contrib.gis.geos import Point
from django.forms import *
from .forms import *
from compte.views import *
from compte.models import *

def add_node(request, pseudo ,client_id):
    client = Client.objects.get(identifiant=client_id)
    print(client)

    if request.method == 'POST':
        
        mylatitude = request.POST.get('Latitude') 
        mylongitude = request.POST.get('Longitude') 
        point = Point(x=float(mylongitude), y=float(mylatitude))
        name = request.POST.get('name') 
        instnace_node=nodes(Position=point, Name=name, client=client)
        instnace_node.save()
        client.node=instnace_node
        # print(nodeee)
        # instance_client = Client(node=instnace_node)
        # instance_client.save()
        client.save()
        
        
     



        return redirect('home')

   

    return render(request, 'pagesuperviseur.html')


def all_nodes(request):
    
    
    if request.method == 'POST':
        mylatitude = request.POST.get('Latitude') 
        mylongitude = request.POST.get('Longitude') 
        point = Point(x=float(mylongitude), y=float(mylatitude))
        
        node = nodes(Position=point, Latitude=mylatitude, Longitude=mylongitude)
        node.save()



        return redirect('all_nodes')

    all_nodes = nodes.objects.all()

    return render(request, 'allnodes.html', {'all_nodes': all_nodes})


