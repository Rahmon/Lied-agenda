from agenda.webservice.models import Contato
from rest_framework import viewsets
from agenda.webservice.serializers import ContatoSerializer
 
class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
