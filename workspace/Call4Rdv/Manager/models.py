from django.db import models

# Create your models here.
class Commercial(models.Model):
    
    nom = models.CharField(max_length=255, blank = True, null = False)
    prenom = models.CharField(max_length=255, blank = True, null = False)
    username = models.CharField(max_length=255, blank = True, null = False)
    password = models.CharField(max_length=255, blank = True, null = False)
    
    isActive = models.BooleanField(default = False, blank = False)
    email = models.CharField(max_length=255, blank = True, null = True)
    
    def __unicode__(self):
        return self.nom+" "+self.prenom