from django.urls import path

from .views import ShelterHomeView


app_name = 'shedter'

urlpatterns = [
    path('', ShelterHomeView.as_view(), name='home'),
]
