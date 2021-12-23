from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']


