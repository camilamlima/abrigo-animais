from django.urls import path

from .views import (
    AdoptionAnimalView,
    AdoptionListView,
    AnimalDetailView,
    AnimalListView,
    PartnerDetailView,
    PartnerListView,
    ShelterDetailView,
    ShelterHomeView,
    ShelterListView,
)


app_name = 'shelter'

urlpatterns = [
    path('', ShelterHomeView.as_view(), name='home'),
    path('adocoes/', AdoptionListView.as_view(), name="list_adoptions"),
    path('animais/', AnimalListView.as_view(), name="list_animals"),
    path(
        'animais/<uuid:id>', AnimalDetailView.as_view(), name="detail_animal"
    ),
    path(
        'animais/<uuid:id>/adotar',
        AdoptionAnimalView.as_view(),
        name="adoption_animal",
    ),
    path('abrigos/', ShelterListView.as_view(), name="list_shelters"),
    path(
        'abrigos/<uuid:id>', ShelterDetailView.as_view(), name="detail_shelter"
    ),
    path(
        'parceiros/',
        PartnerListView.as_view(),
        name="list_partners",
    ),
    path(
        'parceiros/<uuid:id>',
        PartnerDetailView.as_view(),
        name="detail_partner",
    ),
]
