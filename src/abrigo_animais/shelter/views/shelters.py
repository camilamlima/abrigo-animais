from typing import Any

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import ShelterModel


class ShelterHomeView(TemplateView):  # type: ignore
    template_name = "shelter/shelter_home.html"


class ShelterListView(ListView):  # type: ignore
    model = ShelterModel
    template_name = "shelter/shelter_list.html"
    paginate_by = 10


class ShelterDetailView(DetailView):  # type: ignore
    model = ShelterModel
    template_name = "shelter/shelter_detail.html"

    def get_object(self) -> Any:
        return self.model.objects.get(pk=self.kwargs['id'])
