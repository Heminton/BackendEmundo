from rest_framework.serializers import ModelSerializer

from .models import Departamento

class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'