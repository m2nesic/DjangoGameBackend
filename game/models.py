from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


User = settings.AUTH_USER_MODEL #only in models, get_user_model() in views.  

def upload_to(instance, filename):
    return 'games/{filename}'.format(filename=filename)

class Game(models.Model):
    title = models.CharField(max_length=220, default='')
    slug = models.SlugField(max_length=250, null=True, blank=False)
    studio = models.CharField(max_length=220, default='')
    year = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(
        _("Image"), upload_to = upload_to, default='games/default.jpg', blank=True)
    gold_average = models.DecimalField(decimal_places=1, max_digits=2, blank=True, null=True)
    no_gold_rating = models.IntegerField(null=True, blank=True, default=0)
    silver_average = models.DecimalField(decimal_places=1, max_digits=2, blank=True, null=True)
    no_silver_rating = models.IntegerField(null=True, blank=True, default=0)

    #override save, pre-save signal

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def new_rating(self, rv, rv2):                                  # functions called to adjust aggregate values with respect to multiple reviews.
        if rv.get('gold__avg'):
            self.gold_average = rv.get('gold__avg')
            self.no_gold_rating = self.no_gold_rating + 1
        if rv2.get('silver__avg'):
            self.silver_average = rv2.get('silver__avg')
            self.no_silver_rating = self.no_silver_rating + 1
        self.save()        

    def remove_rating(self, rv, rv2):                               # functions called to adjust aggregate values with respect to multiple reviews.
        if rv.get('gold__avg'):
            self.gold_average = rv.get('gold__avg')
            self.no_gold_rating = self.no_gold_rating - 1
        if rv2.get('silver__avg'):
            self.silver_average = rv2.get('silver__avg')
            if self.no_silver_rating > 0:
                self.no_silver_rating = self.no_silver_rating - 1
        self.save()

    
    def __str__(self):
        return self.title