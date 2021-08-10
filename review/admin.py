from django.contrib import admin
from . import models

@admin.register(models.Review)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'game', 'id', 'status', 'slug', 'author', 'gold', 'silver')
    prepopulated_fields = {'slug' : ('title',), }
