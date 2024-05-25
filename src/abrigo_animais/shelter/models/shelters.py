from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models import AddressModel, BaseModel, ContactModel


class ShelterModel(BaseModel):
    name = models.CharField(max_length=250, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    website = models.URLField(verbose_name=_('Website'))
    photo = models.ImageField(upload_to='shelters/', verbose_name=_('Photo'))

    class Meta:
        verbose_name = _('Shelter')
        verbose_name_plural = _('Shelters')

    def __str__(self) -> str:
        return f'Shelter {self.name}'


class ShelterContactModel(ContactModel):
    shelter = models.ForeignKey(
        'shelter.ShelterModel',
        on_delete=models.CASCADE,
        verbose_name=_('Shelter'),
        related_name='contacts',
    )

    class Meta:
        verbose_name = _('Shelter Contact')
        verbose_name_plural = _('Shelter Contacts')


class ShelterAddressModel(AddressModel):
    shelter = models.ForeignKey(
        'shelter.ShelterModel',
        on_delete=models.CASCADE,
        verbose_name=_('Shelter'),
        related_name='addresses',
    )

    class Meta:
        verbose_name = _('Shelter Address')
        verbose_name_plural = _('Shelter Addresses')
