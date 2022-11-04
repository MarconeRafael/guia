from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao
class AtracaoSerialiser(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao', 'horaio_fun', 'idade_minima', 'foto']