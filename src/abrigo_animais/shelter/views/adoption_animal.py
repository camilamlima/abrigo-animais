from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView

from ..forms import ResponsibleAddressFormSet, ResponsibleContactFormSet
from ..models import AdoptionModel, AnimalModel, ResponsibleModel


class AdoptionAnimalView(TemplateView, LoginRequiredMixin):  # type: ignore
    template_name = "shelter/adoption_animal.html"

    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        context = {
            'animal': AnimalModel.objects.get(pk=kwargs['id']),
            'contact_formset': ResponsibleContactFormSet(),
            'address_formset': ResponsibleAddressFormSet(),
        }

        return self.render_to_response(context)

    def post(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        animal = AnimalModel.objects.get(pk=kwargs['id'])
        contact_formset = ResponsibleContactFormSet(request.POST)
        address_formset = ResponsibleAddressFormSet(request.POST)

        if contact_formset.is_valid() and address_formset.is_valid():
            responsible, _ = ResponsibleModel.objects.get_or_create(
                user=request.user
            )
            contact_formset.instance = responsible
            contact_formset.save()

            address_formset.instance = responsible
            address_formset.save()

            AdoptionModel.objects.create(
                animal=animal, responsible=responsible
            )

            return self.render_to_response(
                {'message': 'Animal adopted successfully!'}
            )

        return self.render_to_response({'message': 'Error adopting animal!'})
