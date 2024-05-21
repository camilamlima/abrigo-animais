from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class AddressModel(BaseModel):

    street = models.CharField(max_length=250, verbose_name=_('Street'))
    number = models.CharField(max_length=20, verbose_name=_('Number'))
    complement = models.CharField(
        max_length=250, verbose_name=_('Complement'), blank=True, null=True
    )
    neighborhood = models.CharField(
        max_length=250, verbose_name=_('Neighborhood')
    )
    city = models.CharField(max_length=250, verbose_name=_('City'))
    state = models.CharField(max_length=250, verbose_name=_('State'))
    zip_code = models.CharField(max_length=9, verbose_name=_('Zip code'))

    class Meta:
        abstract = True
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
