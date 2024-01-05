from django.apps import AppConfig


class AboutConfig(AppConfig):
    '''
    Configuration class
    Represents the configuration for the 'about' app.
    Defines settings like auto-generated field and name of the app.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
