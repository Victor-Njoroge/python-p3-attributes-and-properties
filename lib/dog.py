#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        if 1 <= len(name) <= 25:
            self.name = name
            self._breed = breed  

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

# Creating an instance of Dog
Snoopy = Dog("Blue", "Pointer")

# Accessing the name attribute
print(Snoopy.name)  # This line was missing a print statement

# Accessing the breed attribute
print(Snoopy.breed)
