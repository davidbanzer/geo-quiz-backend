from rest_framework import serializers
from api.models import Ranking
from api.serializers.user_serializers import UserSerializer

class RankingSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(many=False,read_only=True)
    class Meta:
        model = Ranking
        fields = ('id', 'usuario', 'preguntas_acertadas', 'tiempo', 'fecha', 'semana')