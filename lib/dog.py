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
    def __init__(self, name="Fluffy", breed="Mastiff"):
        try:
            self.name = name
        except ValueError as e:
            print(e)
            self._name = "Fluffy"  # default name if invalid

        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mastiff"  # default breed if invalid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value.strip()) <= 25:
            self._name = value
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
