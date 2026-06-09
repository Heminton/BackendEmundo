from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteModelViewSet(ModelViewSet):
    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer