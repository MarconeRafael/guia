from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerialiser
from django_filters.rest_framework import DjangoFilterBackend

class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerialiser
    filter_backends = (DjangoFilterBackend,)
    filterset_fields =  {'nome': ['startswith'], 'descricao': ['startswith']}