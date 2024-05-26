#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This module provides abstract class Animal and classes Dog and Cat
"""


class Animal(ABC):
    """
    This is class Animal
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
