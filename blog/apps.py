from django.apps import AppConfig


class BlogConfig(AppConfig):
    '''
    Configuration class
    Represents the configuration for the 'blog' app.
    Defines settings like auto-generated field and name of the app.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
