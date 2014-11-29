
from rest_framework import serializers, viewsets
from Manager.models import Commercial



# Serializers define the API representation.
class CommercialSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Commercial
        fields = ('id', 'nom','username')