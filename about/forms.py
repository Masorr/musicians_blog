from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    '''
    Form for collecting collaboration requests.
    The form collects information related to collaboration requests.
    '''
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
