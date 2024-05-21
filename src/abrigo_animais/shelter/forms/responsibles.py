from django import forms

from abrigo_animais.shelter.models import (
    ResponsibleAddressModel,
    ResponsibleContactModel,
    ResponsibleModel,
)


class ResponsibleContactForm(forms.ModelForm):  # type: ignore
    class Meta:
        model = ResponsibleContactModel
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by']


class ResponsibleAddressForm(forms.ModelForm):  # type: ignore
    class Meta:
        model = ResponsibleAddressModel
        exclude = ['created_at', 'updated_at', 'created_by', 'updated_by']


# Definindo os inlines usando inlineformset_factory
ResponsibleContactFormSet = forms.inlineformset_factory(
    ResponsibleModel,
    ResponsibleContactModel,
    form=ResponsibleContactForm,
    extra=1,
)

ResponsibleAddressFormSet = forms.inlineformset_factory(
    ResponsibleModel,
    ResponsibleAddressModel,
    form=ResponsibleAddressForm,
    extra=1,
)
