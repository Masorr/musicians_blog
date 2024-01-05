from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    '''
    Summernote editor settings are applied to the 'description' field.
    The 'has_add_permission' method checks
    if an instance of 'About' already exists. If an instance exists,
    it prevents the addition of new instances to maintain a single instance.
    '''

    summernote_fields = ('description',)

    def has_add_permission(self, request):
        # Check if an instance of About already exists
        if About.objects.exists():
            # If an instance already exists,
            # return False to prevent adding new instances
            return False
        # Allow adding an instance if one doesn't exist yet
        return True


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    '''
    The list display includes the 'message' and 'read' fields for 'CollaborateRequest' instances.
    '''

    list_display = ('message', 'read',)
