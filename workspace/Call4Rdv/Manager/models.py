
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Commercial(User):
    
    nom = models.CharField(max_length = 255, null = True, blank = True)
    """email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)"""

    USERNAME_FIELD = 'email'

    
    def get_absolute_url(self):
        return reverse('indexCommercial')
        
    def __unicode__(self):
        return self.nom
    
    