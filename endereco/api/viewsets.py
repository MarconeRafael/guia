from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializers import EnderecoSerialiser
from django_filters.rest_framework import DjangoFilterBackend


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerialiser
    filter_backends = (DjangoFilterBackend,)
    filterset_fields =  {'cidade': ['startswith'], 'estado': ['startswith'], 'pais': ['startswith']}