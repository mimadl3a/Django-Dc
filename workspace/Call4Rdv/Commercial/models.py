from django.db import models

# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=255, null = False)
    prenom = models.CharField(max_length=255, null = False)
    code = models.CharField(max_length=255, null = False)
    rasinSociale = models.CharField(max_length=255, null = False)
    email = models.CharField(max_length=255, null = False)
    adresse = models.CharField(max_length=255, null = False)
    
    def __unicode__(self):
        return self.nom+" "+self.prenom
    


class Commande(models.Model):
    code = models.CharField(max_length=255, null = False)
    dateCommande = models.DateTimeField(null = False)
    dateReglement = models.DateTimeField(null = False)
    preuveReglement =models.CharField(max_length = 255, null = False)
    totalTTC = models.FloatField(null = False)
    script = models.TextField(null = False)
    nbrRdv = models.IntegerField(null = False)
    fichierProspect = models.BooleanField(null = False, default = False)
    objections = models.TextField(null = False)
    plageHoraire = models.TextField(null = False)
    client = models.ForeignKey(Client)
    
    def __unicode__(self):
        return self.code+" "+self.dateCommande.strftime('%Y-%m-%d')
    