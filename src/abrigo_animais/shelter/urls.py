from django.urls import path

from .views import (
    AdoptAnimalView,
    AnimalDetailView,
    AnimalListView,
    ShelterHomeView,
)


app_name = 'shelter'

urlpatterns = [
    path('', ShelterHomeView.as_view(), name='home'),
    path('animais/', AnimalListView.as_view(), name="list_animals"),
    path(
        'animais/<uuid:id>/adotar/',
        AdoptAnimalView.as_view(),
        name="adopt_animal",
    ),
    path(
        'animais/<uuid:id>', AnimalDetailView.as_view(), name="detail_animal"
    ),
]
