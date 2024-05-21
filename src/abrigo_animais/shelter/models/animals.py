from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models import BaseModel


class AnimalModel(BaseModel):
    class AnimalSpecie(models.TextChoices):  # type: ignore
        DOG = 'DOG', _('Dog')
        CAT = 'CAT', _('Cat')
        BIRD = 'BIRD', _('Bird')
        RODENT = 'RODENT', _('Rodent')
        OUTHER = 'OUTHER', _('Other')

    class AnimalSize(models.TextChoices):  # type: ignore
        SMALL = 'SMALL', _('Small')
        MEDIUM = 'MEDIUM', _('Medium')
        LARGE = 'LARGE', _('Large')

    name = models.CharField(max_length=250, verbose_name=_('Name'))
    age = models.IntegerField(verbose_name=_('Age'))
    breed = models.CharField(max_length=250, verbose_name=_('Breed'))
    specie = models.CharField(
        max_length=50,
        choices=AnimalSpecie.choices,
        default=AnimalSpecie.OUTHER,
        verbose_name=_('Specie'),
    )
    size = models.CharField(
        choices=AnimalSize.choices,
        max_length=50,
        verbose_name=_('Size'),
        default=AnimalSize.MEDIUM,
    )
    weight = models.FloatField(verbose_name=_('Weight'))
    photo = models.ImageField(upload_to='animals/', verbose_name=_('Photo'))

    class Meta:
        verbose_name = _('Animal')
        verbose_name_plural = _('Animals')

    def __str__(self) -> str:
        return f'{self.specie} {self.breed} {self.name}'
