from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models import AddressModel, BaseModel, ContactModel


class ResponsibleModel(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )

    class Meta:
        verbose_name = _('Responsible')
        verbose_name_plural = _('Responsibles')

    def __str__(self) -> str:
        return f'{self.user}'


class ResponsibleContactModel(ContactModel):
    responsible = models.ForeignKey(
        'shelter.ResponsibleModel',
        on_delete=models.CASCADE,
        verbose_name=_('Responsible'),
        related_name='contacts',
    )

    class Meta:
        verbose_name = _('Responsible Contact')
        verbose_name_plural = _('Responsible Contacts')


class ResponsibleAddressModel(AddressModel):
    responsible = models.ForeignKey(
        'shelter.ResponsibleModel',
        on_delete=models.CASCADE,
        verbose_name=_('Responsible'),
        related_name='addresses',
    )

    class Meta:
        verbose_name = _('Responsible Address')
        verbose_name_plural = _('Responsible Addresses')
