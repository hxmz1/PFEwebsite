from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from connexion.forms import *
from connexion.views import *
from compte.models import Data
from django.shortcuts import render
from .mqtt import *

#from .mqtt import start_mqtt_client
import json

from django.http import HttpResponse, JsonResponse

def dashboardclient(request, id):
    return render(request, 'dashboardclient.html', {'id': id})

def mqtt(request):
    node = nodes.objects.get(Name='my_node_name')
    data = Data.objects.filter(nodes=node)
    context = {
        'temperature': data.temperature,
        'humidity': data.humidity,
    }

    return render(request, 'testmqtt.html', context)
    


