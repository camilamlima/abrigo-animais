from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class ContactModel(BaseModel):

    class ContactType(models.TextChoices):  # type: ignore
        EMAIL = 'EMAIL', _('Email')
        PHONE = 'PHONE', _('Phone')
        WHATSAPP = 'WHATSAPP', _('WhatsApp')
        OTHER = 'OTHER', _('Other')

    type = models.CharField(
        max_length=20,
        choices=ContactType.choices,
        verbose_name=_('Type'),
        default=ContactType.OTHER,
    )
    value = models.CharField(max_length=250, verbose_name=_('Value'))

    class Meta:
        abstract = True
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
