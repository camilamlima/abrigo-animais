from django.views.generic.list import ListView

from ..models import AdoptionModel


class AdoptionListView(ListView):  # type: ignore
    model = AdoptionModel
    template_name = "shelter/adoption_list.html"
    paginate_by = 10
