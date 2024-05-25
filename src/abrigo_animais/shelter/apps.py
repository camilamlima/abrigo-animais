from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShelterConfig(AppConfig):  # type: ignore
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abrigo_animais.shelter'
    verbose_name = _('Shelter')
