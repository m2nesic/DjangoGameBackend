from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from game.models import Game
from django.contrib.auth import get_user_model
User = get_user_model()

class GameTest(APITestCase):

    def test_view_games(self):                              # testing the list view
        url = reverse('review_api:game_api:game-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GameTest2(APITestCase):

    def test_detail_games(self):                            # testing the detail view
        self.test_game = Game.objects.create(title='django', slug='mySlug')
        url = reverse('review_api:game_api:game-detail', args=['mySlug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)