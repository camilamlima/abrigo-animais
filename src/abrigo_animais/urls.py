"""
URL configuration for abrigo_animais project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = (
    [
        path(
            '', RedirectView.as_view(pattern_name="shelter:home"), name='home'
        ),
        path('admin/', admin.site.urls),
        path('logout/', LogoutView.as_view(), name='logout'),
        path(
            'social-auth/',
            include('social_django.urls', namespace='social-auth'),
        ),
        path(
            'abrigo/',
            include('abrigo_animais.shelter.urls', namespace='shelter'),
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # noqa
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # noqa
)

# handler500 = 'rest_framework.exceptions.server_error'
# handler404 = 'cog_platform.exceptions.page_not_found'
