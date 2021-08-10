from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from review.models import Review 
from game.models import Game
from django.contrib.auth import get_user_model
User = get_user_model()

class ReviewTest2(APITestCase):
    def test_create_reviews(self):
        self.test_game = Game.objects.create(title='django')
        self.testuser1 = User.objects.create_user(email = 'a@b.com', user_name= 'ab' , first_name = 'a', password = '12345678')
        data =  {"title":'myReview', "slug":"myReview", "author" : 1, "content" : 'myContent',  "game":1 }
        data_bad =  {"title":'', "slug":"", "author" : 1, "content" : '',  "game":1 }
        url = reverse('review_api:createreview')
        response = self.client.post(url, data)
        response_bad = self.client.post(url, data_bad)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_bad.status_code, status.HTTP_400_BAD_REQUEST)

class ReviewTest(APITestCase):
    
    def test_view_reviews(self):
        url = reverse('review_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ReviewTest3(APITestCase):
    
    def test_search_reviews(self):
        test_game = Game.objects.create(title='django')
        testuser1 = User.objects.create_user(email = 'a@b.com', user_name= 'ab' , first_name = 'a', password = '12345678')
        test_review = Review.objects.create(game=test_game, title='Title', slug='mySlug', content = 'Content', author_id = 1, status='published')

        url = reverse('review_api:detailreview', args=['mySlug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
