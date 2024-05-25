from .adoption_animal import AdoptionAnimalView
from .adoptions import AdoptionDetailView, AdoptionListView
from .animals import AnimalDetailView, AnimalListView
from .partners import PartnerDetailView, PartnerListView
from .shelters import ShelterDetailView, ShelterHomeView, ShelterListView


__all__ = [
    'AdoptionAnimalView',
    'AdoptionListView',
    'AnimalListView',
    'AdoptionDetailView',
    'AnimalDetailView',
    'ShelterHomeView',
    'ShelterListView',
    'ShelterDetailView',
    'PartnerListView',
    'PartnerDetailView',
]
