from django.db import models
from django.utils.translation import gettext_lazy as _

from abrigo_animais.core.models import BaseModel


class AdoptionModel(BaseModel):
    class AdoptionStatus(models.TextChoices):  # type: ignore
        PENDING = 'pending', _('Pending')
        APPROVED = 'approved', _('Approved')
        REJECTED = 'rejected', _('Rejected')
        CANCELED = 'canceled', _('Canceled')

    animal = models.ForeignKey('shelter.AnimalModel', on_delete=models.CASCADE)
    responsible = models.ForeignKey(
        'shelter.ResponsibleModel', on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=50,
        choices=AdoptionStatus.choices,
        default=AdoptionStatus.PENDING,
    )

    class Meta:
        verbose_name = _('Adoption')
        verbose_name_plural = _('Adoptions')

    def __str__(self) -> str:
        return f'{self.animal} - {self.responsible} - {self.status}'
