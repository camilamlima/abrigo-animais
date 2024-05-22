from typing import Any, Tuple

from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest


def _set_defaults_values_fields(
    obj: Any, defaults_fields: Tuple[Tuple[str, Tuple[str, ...]], ...]
) -> None:
    for field, default_value in defaults_fields:
        setattr(obj, field, getattr(obj, field, ()) + default_value)


class BaseAdmin(admin.ModelAdmin):  # type: ignore
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults_fields = (
            (
                'list_display',
                ('created_at', 'created_by', 'updated_at', 'updated_by'),
            ),
            ('list_filter', ('updated_at',)),
            (
                'readonly_fields',
                ('created_at', 'created_by', 'updated_at', 'updated_by'),
            ),
        )

        super().__init__(*args, **kwargs)
        _set_defaults_values_fields(self, defaults_fields)

    def save_model(
        self, request: HttpRequest, obj: Any, form: ModelForm, change: bool
    ) -> None:
        obj.updated_by = request.user
        if not change:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)

    def save_formset(
        self,
        request: HttpRequest,
        form: ModelForm,
        formset: ModelForm,
        change: bool,
    ) -> None:
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()

        for instance in instances:
            instance.updated_by = request.user
            if not change:
                instance.created_by = request.user
            instance.save()

        formset.save_m2m()


class BaseInline:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults_fields = (
            (
                'readonly_fields',
                ('created_at', 'created_by', 'updated_at', 'updated_by'),
            ),
        )
        super().__init__(*args, **kwargs)
        _set_defaults_values_fields(self, defaults_fields)


class BaseTabularInline(BaseInline, admin.TabularInline):  # type: ignore
    extra = 0


class BaseStackedInline(BaseInline, admin.StackedInline):  # type: ignore
    extra = 0

