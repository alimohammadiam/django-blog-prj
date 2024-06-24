from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'publish', 'atatus']
    ordering = ['title', 'publish']
    list_filter = ['status', 'publish', 'author']
    search_fields = ['title', 'description']
#   raw_id_fields = 'author'
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ['title']}
    list_editable = 'publish'
#    list_display_links = 'author'
