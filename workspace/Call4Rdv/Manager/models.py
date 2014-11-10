from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

# Create your models here.
class Commercial(User, models.Model):
    def get_absolute_url(self):
        return reverse('indexCommercial')  
    def __unicode__(self):
        return self.nom+" "+self.prenom