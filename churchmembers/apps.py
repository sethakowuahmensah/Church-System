# churchmembers/apps.py
from django.apps import AppConfig

class ChurchMembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'churchmembers'

    def ready(self):
        import churchmembers.signals  # Load signals