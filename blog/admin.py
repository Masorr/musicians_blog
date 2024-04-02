from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
    Admin configuration for Post model.

    It includes display preferences, search-related fields,
    filtration capabilities, and the configuration for
    Summernote editor applied to the 'content' field.
    '''

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    The list display includes the 'body', 'author', 'post',
    'approved' and 'created_on'
    fields for 'Comment' instances.
    '''
    list_display = ('body', 'author', 'post', 'approved', 'created_on')

# Register your models here.
admin.site.register(Profile)
