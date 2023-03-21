from rest_framework import viewsets, permissions
from api.models import Ranking
from api.serializers import RankingSerializer
from rest_framework.response import Response

class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer

    def list(self, request, *args, **kwargs):
        queryset = Ranking.objects.all().order_by('-preguntas_acertadas', 'tiempo')
        serializer = RankingSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data            
        nuevo_puntaje = Ranking.objects.create(usuario_id=data["usuario_id"],preguntas_acertadas=data["preguntas_acertadas"], tiempo=data["tiempo"], semana=data["semana"])
        nuevo_puntaje.save()
        serializer = RankingSerializer(nuevo_puntaje)
        return Response(serializer.data)

    
