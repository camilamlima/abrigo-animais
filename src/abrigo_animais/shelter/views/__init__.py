from .adoption_animal import AdoptionAnimalView
from .adoptions import AdoptionListView
from .animals import AnimalDetailView, AnimalListView
from .partners import PartnerDetailView, PartnerListView
from .shelters import ShelterDetailView, ShelterHomeView, ShelterListView


__all__ = [
    'AdoptionAnimalView',
    'AdoptionListView',
    'AnimalListView',
    'AnimalDetailView',
    'ShelterHomeView',
    'ShelterListView',
    'ShelterDetailView',
    'PartnerListView',
    'PartnerDetailView',
]
