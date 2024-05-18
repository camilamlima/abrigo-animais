from django.contrib import admin

from .models import AddressModel, ContactModel


class AddressAdmin(admin.ModelAdmin): ...  # type: ignore


class ContactAdmin(admin.ModelAdmin): ...  # type: ignore


admin.site.register(AddressModel, AddressAdmin)
admin.site.register(ContactModel, ContactAdmin)
