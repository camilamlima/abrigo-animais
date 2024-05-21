from django.apps import AppConfig


class CoreConfig(AppConfig):  # type: ignore
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abrigo_animais.core'
    verbose_name = 'Core'
