
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/home/imad/workspace/Call4Rdv/Manager/static/media/fichiers')

# Create your models here.
class Commercial(User):
    
    nom = models.CharField(max_length = 255, null = True, blank = True)
    data = models.FileField(storage=fs, null=True)
    """email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)"""

    USERNAME_FIELD = 'email'

    
    def get_absolute_url(self):
        return reverse('indexCommercial')
        
    def __unicode__(self):
        return self.nom
    
    
class DataCommercial(models.Model):
    Civ = models.CharField(max_length=255, blank = True, null = True)
    Nom = models.CharField(max_length=255, blank = True, null = True)
    Prenom = models.CharField(max_length=255, blank = True, null = True)
    Adresse1 = models.CharField(max_length=255, blank = True, null = True)
    Adresse2 = models.CharField(max_length=255, blank = True, null = True)
    Adresse3 = models.CharField(max_length=255, blank = True, null = True)
    Adresse4 = models.CharField(max_length=255, blank = True, null = True)
    Cp = models.CharField(max_length=255, blank = True, null = True)
    Ville = models.CharField(max_length=255, blank = True, null = True)
    Email = models.CharField(max_length=255, blank = True, null = True)
    