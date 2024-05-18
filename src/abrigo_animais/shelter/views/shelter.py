from typing import Any

from django.views.generic.base import TemplateView


class ShelterHomeView(TemplateView):  # type: ignore
    template_name = "shelter/shelter_home.html"

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        return context
