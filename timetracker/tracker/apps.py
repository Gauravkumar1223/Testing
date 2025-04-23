from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'

# apps.py
def ready(self):
    import tracker.signals  # Replace with your app name

