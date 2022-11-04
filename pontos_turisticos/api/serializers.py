from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import pontos_turistico
from atracoes.api.serializers import AtracaoSerialiser
from avaliacoes.api.serializers import AvaliacaoSerialiser
from comentarios.api.serializers import ComentarioSerialiser
from endereco.api.serializers import EnderecoSerialiser
from rest_framework.fields import SerializerMethodField


class pontos_turisticoSerialiser(ModelSerializer):
    atracoes = AtracaoSerialiser(many=True)
    comentarios = ComentarioSerialiser(many=True)
    avaliacoes = AvaliacaoSerialiser(many=True)
    endereco = EnderecoSerialiser(many=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = pontos_turistico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa', 'descricao_completa2'
                  ]

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)