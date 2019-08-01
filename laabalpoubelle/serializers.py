from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import *




class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('nom', 'prenom', 'adresse', 'telephone','zones')


class PoubellesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poubelles
        fields = ('nom','types')



class ZonesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zones
        fields = ('nom',)




class CommandeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commandes
        fields = ('date_add', 'clients', 'poubelles')