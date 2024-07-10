from django.contrib import admin
from .models import *

# Register your models here.

admin.sites.AdminSite.site_header = 'پنل مدیریت جنگو'
admin.sites.AdminSite.site_title = 'پنل'
admin.sites.AdminSite.index_title = 'پنل مدیریت'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['status', 'publish', 'author']
    search_fields = ['title', 'description']
#   raw_id_fields = 'author'
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['status']
#    list_display_links = 'author'


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'body']
    list_editable = ['active']
    