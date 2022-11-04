from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerialiser
from django_filters.rest_framework import DjangoFilterBackend


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerialiser
    filter_backends = (DjangoFilterBackend,)
    filterset_fields =  {'data': ['startswith']}