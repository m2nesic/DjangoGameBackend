from django.test import TestCase
from django.contrib.auth import get_user_model
from review.models import Review
from game.models import Game

User = get_user_model()
# Create your tests here.
class Test_Create_Review(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_game = Game.objects.create(title='django')
        testuser1 = User.objects.create_user(email = 'a@b.com', user_name= 'ab' , first_name = 'a', password = '12345678')
        test_review = Review.objects.create(game=test_game, title='Title', content = 'Content', author_id = 1, status='published', gold = 2, silver = 3)

    def test_review_content(self):
        review = Review.reviewobjects.get(id=1)
        game = Game.objects.get(id=1)
        author = f'{review.author}'
        title = f'{review.title}'
        content = f'{review.content}'
        status = f'{review.status}'

        self.assertEqual(author, 'ab')
        self.assertEqual(title, 'Title')
        self.assertEqual(content, 'Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(review), title)                                
        self.assertEqual(str(game), 'django')

    def test_review_delete(self):
        Game.objects.all().delete()
        Review.objects.all().delete()                                

        game_count = Game.objects.all().count()
        review_count = Review.objects.all().count()

        self.assertEqual(game_count, 0)
        self.assertEqual(review_count, 0)