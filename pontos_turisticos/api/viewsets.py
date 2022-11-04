from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import pontos_turistico
from .serializers import pontos_turisticoSerialiser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class pontos_turisticoViewSet(ModelViewSet):
    queryset = pontos_turistico.objects.all()
    serializer_class = pontos_turisticoSerialiser
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {'nome': ['startswith'], 'descricao': ['startswith']}

    # abaixo reimplemento os comportamentos padros das classes mas é possivel modificar
    def list(self, request, *args, **kwargs):
        return super(pontos_turisticoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(pontos_turisticoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(pontos_turisticoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(pontos_turisticoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(pontos_turisticoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(pontos_turisticoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass