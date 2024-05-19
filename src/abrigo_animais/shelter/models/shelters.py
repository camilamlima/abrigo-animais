from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models.base import BaseModel


class ShelterModel(BaseModel):

    name = models.CharField(max_length=250, verbose_name=_('Name'))
    contacts = models.ManyToManyField(
        'core.ContactModel',
        verbose_name=_('Contacts'),
        related_name='shelters',
    )
    adresses = models.ManyToManyField(
        'core.AddressModel',
        verbose_name=_('Sdresses'),
        related_name='shelters',
    )

    class Meta:
        verbose_name = _('Shelter')
        verbose_name_plural = _('Shelters')

    def __str__(self) -> str:
        return f'Shelter {self.name}'
