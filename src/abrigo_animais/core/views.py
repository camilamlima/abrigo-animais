from typing import Any

from django.urls import reverse
from django.views.generic.base import RedirectView


class LoginView(RedirectView):  # type: ignore
    pattern_name = "social-auth:begin"

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> Any:
        return reverse(self.pattern_name, args=['google-oauth2'])
