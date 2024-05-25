from typing import Any

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..forms import ResponsibleAddressFormSet, ResponsibleContactFormSet
from ..models import AdoptionModel, AnimalModel, ResponsibleModel


class AdoptionAnimalView(LoginRequiredMixin, TemplateView):  # type: ignore
    login_url = settings.LOGIN_URL
    redirect_field_name = "redirect_to"
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

            adoption = AdoptionModel.objects.create(
                animal=animal, responsible=responsible
            )
            return redirect(
                reverse('shelter:detail_adoption', args=[adoption.id])
            )

        context = {
            'animal': animal,
            'contact_formset': contact_formset,
            'address_formset': address_formset,
        }
        return self.render_to_response(context)
