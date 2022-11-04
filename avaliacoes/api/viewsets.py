from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerialiser
from django_filters.rest_framework import DjangoFilterBackend

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerialiser
    filter_backends = (DjangoFilterBackend,)
    filterset_fields =  {'nota': ['startswith'], 'data': ['startswith']}