from django.db import models

# Create your models here.
from django.contrib import admin
from django.contrib.auth.models import AbstractUser

# Create your models here.r



class Clients(models.Model):
    	
    	nom     = models.CharField(max_length=255)
    	prenom     = models.CharField(max_length=100)
    	adresse     = models.CharField(max_length=100)
    	telephone     = models.CharField(max_length=100)
    	def __str__(self):
	        return "{0}".format(self.prenom)




class Reclamation(models.Model):
    	
    	nom     = models.CharField(max_length=255)
    	prenom     = models.CharField(max_length=100)
    	objets     = models.CharField(max_length=100)
    	def __str__(self):
	        return "{0}".format(self.objets)

class Critique(models.Model):
    	
    	nom     = models.CharField(max_length=255)
    	prenom     = models.CharField(max_length=100)
    	objets     = models.CharField(max_length=100)
    	def __str__(self):
	        return "{0}".format(self.objets)

class Zones(models.Model):

		nom = models.CharField(max_length=255)
		def __all__(self):
			return "{0}".format(self.nom,)


class Typespoubelle(models.Model):

		types = models.CharField(max_length=255)
		def __all__(self):
			return "{0}".format(self.types,)

class Poubelles(models.Model):
		
		nom = models.CharField(max_length=255)
		types = models.CharField(max_length=255)
		def __str__(self):
			return "{0}".format(self.nom)

class Commandes(models.Model):
		date_add = models.DateField()
		clients = models.ForeignKey('Clients', related_name="Clients", on_delete=models.CASCADE)
		poubelles = models.ForeignKey('Poubelles', related_name="Poubelles", on_delete=models.CASCADE)
		zones = models.ForeignKey('Zones', related_name="Zones", on_delete=models.CASCADE)