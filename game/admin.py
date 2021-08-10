from django.contrib import admin
from .models import Game

# register the game object with the slug field pre-populated

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',), }
    pass

