from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.


class ClientsViewSet(viewsets.ModelViewSet):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class PoubellesViewSet(viewsets.ModelViewSet):

    queryset = Poubelles.objects.all()
    serializer_class = PoubellesSerializer   




class ZonesViewSet(viewsets.ModelViewSet):

    queryset = Zones.objects.all()
    serializer_class = ZonesSerializer


class CommandeViewSet(viewsets.ModelViewSet):

    queryset = Commandes.objects.all()
    serializer_class = CommandeSerializer

