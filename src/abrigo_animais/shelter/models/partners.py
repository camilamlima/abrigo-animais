from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models import AddressModel, BaseModel, ContactModel


class PartnerModel(BaseModel):
    name = models.CharField(max_length=250, verbose_name=_('Name'))
    description = models.TextField(
        verbose_name=_('Description'), blank=True, null=True
    )
    shelter = models.ForeignKey(
        'shelter.ShelterModel', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')

    def __str__(self) -> str:
        return f'Partner {self.name}'


class PartnerContactModel(ContactModel):
    partner = models.ForeignKey(
        'shelter.PartnerModel',
        on_delete=models.CASCADE,
        verbose_name=_('Partner'),
        related_name='contacts',
    )

    class Meta:
        verbose_name = _('Partner Contact')
        verbose_name_plural = _('Partner Contacts')


class PartnerAddressModel(AddressModel):
    partner = models.ForeignKey(
        'shelter.PartnerModel',
        on_delete=models.CASCADE,
        verbose_name=_('Partner'),
        related_name='addresses',
    )

    class Meta:
        verbose_name = _('Partner Address')
        verbose_name_plural = _('Partner Addresses')
