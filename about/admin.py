from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

    def has_add_permission(self, request):
        # Check if an instance of About already exists
        if About.objects.exists():
            # If an instance already exists, return False to prevent adding new instances
            return False
        # Allow adding an instance if one doesn't exist yet
        return True