from django.contrib import admin

from abrigo_animais.core.admin import (
    BaseAdmin,
    BaseStackedInline,
    BaseTabularInline,
)

from .models import (
    AnimalModel,
    ResponsibleAddressModel,
    ResponsibleContactModel,
    ResponsibleModel,
    ShelterAddressModel,
    ShelterContactModel,
    ShelterModel,
)


class AnimalAdmin(BaseAdmin):
    list_display = ('name', 'specie', 'breed', 'size', 'weight')
    list_filter = ('specie', 'size')


class ShelterAdmin(BaseAdmin):
    list_display = ('name',)

    class ShelterContactInline(BaseTabularInline):
        model = ShelterContactModel

    class ShelterAddressInline(BaseStackedInline):
        model = ShelterAddressModel

    inlines = (ShelterContactInline, ShelterAddressInline)


class ResponsibleAdmin(BaseAdmin):
    class ResponsibleContactInline(BaseTabularInline):
        model = ResponsibleContactModel

    class ResponsibleAddressInline(BaseStackedInline):
        model = ResponsibleAddressModel

    inlines = (ResponsibleContactInline, ResponsibleAddressInline)


admin.site.register(AnimalModel, AnimalAdmin)
admin.site.register(ShelterModel, ShelterAdmin)
admin.site.register(ResponsibleModel, ResponsibleAdmin)
