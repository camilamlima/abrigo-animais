import uuid
from typing import Any

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):  # type: ignore

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at')
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
        related_query_name="%(app_label)s_%(class)ss_created_by",
        default=None,
        null=True,
        verbose_name=_('Created by'),
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_updated_by",
        related_query_name="%(app_label)s_%(class)ss_updated_by",
        default=None,
        null=True,
        verbose_name=_('Updated by'),
    )

    class Meta:
        abstract = True
        ordering = ['id']

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.updated_at = timezone.now()
        if self.created_by_id is None:
            self.created_by = self.updated_by
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"
