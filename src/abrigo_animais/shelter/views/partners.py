from typing import Any

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import PartnerModel


class PartnerListView(ListView):  # type: ignore
    model = PartnerModel
    template_name = "shelter/partner_list.html"
    paginate_by = 10


class PartnerDetailView(DetailView):  # type: ignore
    model = PartnerModel
    template_name = "shelter/partner_detail.html"

    def get_object(self) -> Any:
        return self.model.objects.get(pk=self.kwargs['id'])
