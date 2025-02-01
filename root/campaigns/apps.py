from django.apps import AppConfig


class CampaignsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "root.campaigns"

    def ready(self):
        import root.campaigns.signals  # Import the signals
