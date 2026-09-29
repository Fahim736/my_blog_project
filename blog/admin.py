from django.contrib import admin
from .models import Post, Comment, Rating

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'score')