from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import AnimalModel


class AnimalListView(ListView):  # type: ignore
    model = AnimalModel
    template_name = "shelter/animal_list.html"
    paginate_by = 10


class AnimalDetailView(DetailView):  # type: ignore
    model = AnimalModel
    template_name = "shelter/animal_detail.html"

    def get_object(self) -> Any:
        return self.model.objects.get(pk=self.kwargs['id'])


class AdoptAnimalView(TemplateView, LoginRequiredMixin):  # type: ignore
    template_name = "shelter/adopt_animal.html"
