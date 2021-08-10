from rest_framework import serializers
from game.models import Game
from django.conf import settings


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','title','slug','studio','year','picture','gold_average','no_gold_rating','silver_average','no_silver_rating')
