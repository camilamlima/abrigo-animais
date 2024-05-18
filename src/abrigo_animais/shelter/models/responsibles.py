from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models.base import BaseModel


class ResponsibleModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    contacts = models.ManyToManyField(
        'core.ContactModel',
        verbose_name=_('Contacts'),
        related_name='responsibles',
    )
    adresses = models.ManyToManyField(
        'core.AddressModel',
        verbose_name=_('Sdresses'),
        related_name='responsibles',
    )

    class Meta:
        verbose_name = _('Responsible')
        verbose_name_plural = _('Responsibles')
