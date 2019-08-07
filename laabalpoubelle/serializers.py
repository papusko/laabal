from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import *




class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('nom', 'prenom', 'adresse', 'telephone')


class ReclamationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reclamation
        fields = ('nom', 'prenom', 'objets')

class CritiqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Critique
        fields = ('nom', 'prenom', 'objets')        


class TypespoubelleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Typespoubelle
        fields = ('types',)


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
        fields = ('date_add', 'clients', 'poubelles','zones')