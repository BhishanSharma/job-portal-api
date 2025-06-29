from django.apps import AppConfig


class ApplicationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'application_app'

    def ready(self):
        import application_app.signals
