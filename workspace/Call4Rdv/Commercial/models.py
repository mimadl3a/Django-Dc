from django.db import models
from datetime import datetime

# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=255, null = False, default = "")
    prenom = models.CharField(max_length=255, null = False, default = "", blank=True)
    code = models.CharField(max_length=255, null = False, default = "")
    raisonSociale = models.CharField(max_length=255, null = True, default = "", blank=True)
    email = models.CharField(max_length=255, null = False, default = "")
    adresse = models.CharField(max_length=255, null = False, default = "")
                
    def __unicode__(self):
        return self.nom+" "+self.prenom
    


class Commande(models.Model):
    code = models.CharField(max_length=255, null = False)
    dateCommande = models.DateTimeField(null = False, default = datetime.now())
    dateReglement = models.DateTimeField(null = True)
    preuveReglement =models.CharField(max_length = 255, null = True)
    totalTTC = models.FloatField(null = False)
    script = models.TextField(null = False)
    nbrRdv = models.IntegerField(null = False)
    fichierProspect = models.BooleanField(null = False, default = False)
    objections = models.TextField(null = False)
    plageHoraire = models.TextField(null = False)
    client = models.ForeignKey(Client)
    
    
    def __unicode__(self):
        return self.code+" "+self.dateCommande.strftime('%Y-%m-%d')
    
    
    
    
class Calendrier(models.Model):
    title = models.CharField(max_length=255, null = False, default = "")
    description = models.CharField(max_length=255, null = False, default = "")
    start = models.CharField(max_length=255, null = False, default = "")
    end = models.CharField(max_length=255, null = False, default = "")
    
    def __unicode__(self):
        return self.title
    
    
    
    
    
    