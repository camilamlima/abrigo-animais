from django.views.generic.base import TemplateView


class ShelterDonationView(TemplateView):  # type: ignore
    template_name = 'shelter/shelter_donation.html'
