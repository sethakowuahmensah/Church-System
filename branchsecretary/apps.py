# branchsecretary/apps.py
from django.apps import AppConfig

class BranchSecretaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'branchsecretary'

    def ready(self):
        import branchsecretary.models  # Load signals