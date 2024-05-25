from typing import Any

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import AdoptionModel


class AdoptionListView(ListView):  # type: ignore
    model = AdoptionModel
    template_name = "shelter/adoption_list.html"
    paginate_by = 10


class AdoptionDetailView(DetailView):  # type: ignore
    model = AdoptionModel
    template_name = "shelter/adoption_detail.html"

    def get_object(self) -> Any:
        return self.model.objects.get(pk=self.kwargs['id'])
