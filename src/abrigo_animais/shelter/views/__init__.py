from .adoption_animal import AdoptionAnimalView
from .adoptions import AdoptionListView
from .animals import AnimalDetailView, AnimalListView
from .shelter import ShelterDetailView, ShelterHomeView, ShelterListView
from .shelter_donation import ShelterDonationView


__all__ = [
    'AdoptionAnimalView',
    'AdoptionListView',
    'AnimalListView',
    'AnimalDetailView',
    'ShelterHomeView',
    'ShelterListView',
    'ShelterDetailView',
    'ShelterDonationView',
]
