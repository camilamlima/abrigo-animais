from django.contrib import admin

from abrigo_animais.core.admin import (
    BaseAdmin,
    BaseStackedInline,
    BaseTabularInline,
)

from .models import (
    AnimalModel,
    CareModel,
    PartnerAddressModel,
    PartnerContactModel,
    PartnerModel,
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

    class CareInline(BaseTabularInline):
        model = CareModel

    inlines = (CareInline,)


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


class PartnerAdmin(BaseAdmin):
    class PartnerContactInline(BaseTabularInline):
        model = PartnerContactModel

    class PartnerAddressInline(BaseStackedInline):
        model = PartnerAddressModel

    inlines = (PartnerContactInline, PartnerAddressInline)


admin.site.register(AnimalModel, AnimalAdmin)
admin.site.register(ShelterModel, ShelterAdmin)
admin.site.register(ResponsibleModel, ResponsibleAdmin)
admin.site.register(PartnerModel, PartnerAdmin)
