from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
import Commercial

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        
        
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

# Serializers define the API representation.
class CommandeSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.RelatedField()
    
    class Meta:
        model = Commercial.models.Commande
        fields = ('id', 'code', 'dateCommande','client')
        
        
# ViewSets define the view behavior.
class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commercial.models.Commande.objects.all()
    serializer_class = CommandeSerializer
    