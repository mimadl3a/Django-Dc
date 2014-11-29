from rest_framework import serializers, viewsets
from Manager.models import Commercial
from api.models import CommercialSerializer

# Create your views here.


# ViewSets define the view behavior.
class CommercialViewSet(viewsets.ModelViewSet):
    queryset = Commercial.objects.all()
    serializer_class = CommercialSerializer