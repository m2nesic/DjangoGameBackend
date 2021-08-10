from django.db import models
from django.conf import settings
from django.db.models.deletion import PROTECT
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.aggregates import Avg
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


from game.models import Game

options = {
    ('draft', 'Draft'),
    ('published', 'Published'),
}

def upload_to(instance, filename):                              #difficult to test
    return 'reviews/{filename}'.format(filename=filename)

class Review(models.Model):
    class ReviewObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    game = models.ForeignKey(Game, on_delete= models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(
        _("Image"), upload_to = upload_to, default='reviews/default.jpg', blank=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null=True, blank=False)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_posts')
    status = models.CharField(max_length=10, choices=options, default='published') 
    gold = models.IntegerField(default = 1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    silver = models.IntegerField(default = 1,validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    objects = models.Manager()
    reviewobjects = ReviewObjects()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    
    
@receiver(post_save, sender=Review)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        qs_g = Review.objects.filter(status = 'published').aggregate(Avg('gold'))
        qs_s = Review.objects.filter(status = 'published').aggregate(Avg('silver'))
        instance.game.new_rating(qs_g, qs_s)

@receiver(post_delete, sender=Review)
def post_save_receiver(sender, instance, *args, **kwargs):
    qs_g = Review.objects.filter(status = 'published').aggregate(Avg('gold'))
    qs_s = Review.objects.filter(status = 'published').aggregate(Avg('silver'))
    instance.game.remove_rating(qs_g, qs_s)
