from django.contrib import admin

from .models import ResponsibleModel, ShelterModel


class ShelterAdmin(admin.ModelAdmin): ...  # type: ignore


class ResponsibleAdmin(admin.ModelAdmin): ...  # type: ignore


admin.site.register(ShelterModel, ShelterAdmin)
admin.site.register(ResponsibleModel, ResponsibleAdmin)
