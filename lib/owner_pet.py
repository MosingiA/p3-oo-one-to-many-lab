# lib/owner_pet.py

class Pet:
    # Class-level list of valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Class variable to store all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type

        # Validate optional owner
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")
        self.owner = owner

        # Track all pets
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets owned by this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign a Pet to this owner"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
