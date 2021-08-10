from game.models import Game
from .serializers import GameSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework import viewsets 
from django.shortcuts import get_object_or_404

# Create your views here.

class GameList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer

    def get_queryset(self):     #override
        return Game.objects.all()

    def get_object(self, queryset=None, **kwargs):      # return single object based on parameter entered in url
        item = self.kwargs.get('pk')        
        return get_object_or_404(Game, slug=item)

