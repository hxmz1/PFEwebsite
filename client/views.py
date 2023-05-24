from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from connexion.forms import *
from connexion.views import *
from compte.models import *
from django.shortcuts import render
from .mqtt import *
from django.http import *


import json

from django.http import HttpResponse, JsonResponse

def dashboardclient(request,id):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    client= Client.objects.get(id=id)
    name=client.nom
    
    return render(request, 'dashboardclient.html', {'id': id, 'nom':name})




def mqtt(request, id):
    client= Client.objects.get(id=id)
    # node = nodes.objects.all()
    # my_node= node.objects.get()
    
    node = nodes.objects.filter(client=client).order_by('-id').first()
    
    data = Data.objects.filter(nodes=node).order_by('-IdData').first()
    print(data)
    print("------------------------------")
    tem=data.temperature
    print("******************************")
    print(tem)
    print("//////////////")
    hum=data.humidity
    print(hum)
    print(id)
    context = {
        'temperature': tem,
        'humidity': hum,
        'id' : id,
    }

    return render(request, 'testmqtt.html', context)


def mqtt_two(request, id):
    client = Client.objects.get(id=id)
    node = nodes.objects.filter(client=client).order_by('-id').first()
    data = Data.objects.filter(nodes=node).order_by('-IdData').first()
    tem = data.temperature
    hum = data.humidity
    dattta = []
    dattta.append({
        'temperature': tem,
        'humidity': hum,
    })
    print("hhhhhhhhhhhhhhhhhhhhhhh")
    print(dattta)

    return JsonResponse(dattta, safe=False)
    


