from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario
class ComentarioSerialiser(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'usuario', 'comentario', 'data', 'aprovado']