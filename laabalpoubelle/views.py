from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.


class ClientsViewSet(viewsets.ModelViewSet):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ReclamationViewSet(viewsets.ModelViewSet):

    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer

class CritiqueViewSet(viewsets.ModelViewSet):

    queryset = Critique.objects.all()
    serializer_class = CritiqueSerializer


class PoubellesViewSet(viewsets.ModelViewSet):

    queryset = Poubelles.objects.all()
    serializer_class = PoubellesSerializer   


class TypespoubelleViewSet(viewsets.ModelViewSet):

    queryset = Typespoubelle.objects.all()
    serializer_class = TypespoubelleSerializer


class ZonesViewSet(viewsets.ModelViewSet):

    queryset = Zones.objects.all()
    serializer_class = ZonesSerializer


class CommandeViewSet(viewsets.ModelViewSet):

    queryset = Commandes.objects.all()
    serializer_class = CommandeSerializer

