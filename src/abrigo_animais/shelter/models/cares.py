from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models import BaseModel


class CareModel(BaseModel):
    class CareType(models.TextChoices):  # type: ignore
        FOOD = 'FOOD', _('Food')
        DRUG = 'DRUG', _('Drug')
        OTHER = 'OTHER', _('Other')

    animal = models.ForeignKey('shelter.AnimalModel', on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_('Description'))
    care_type = models.CharField(
        max_length=50,
        choices=CareType.choices,
        verbose_name=_('Care type'),
        default=CareType.OTHER,
    )

    class Meta:
        verbose_name = _('Care')
        verbose_name_plural = _('Cares')
