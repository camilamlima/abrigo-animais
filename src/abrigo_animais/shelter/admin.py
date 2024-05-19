from django.contrib import admin

from abrigo_animais.core.admin import BaseAdmin

from .models import AnimalModel, ResponsibleModel, ShelterModel


class ShelterAdmin(BaseAdmin):
    list_display = ('name',)


class AnimalAdmin(BaseAdmin):
    list_display = ('name', 'specie', 'breed', 'size', 'weight')
    list_filter = ('specie', 'size')


class ResponsibleAdmin(admin.ModelAdmin): ...  # type: ignore


admin.site.register(ShelterModel, ShelterAdmin)
admin.site.register(AnimalModel, AnimalAdmin)
admin.site.register(ResponsibleModel, ResponsibleAdmin)
