from django.apps import AppConfig


class TrequestConfig(AppConfig):
    name = 'Trequest'

    def ready(self):
        import Trequest.signals