from abc import ABC, abstractmethod


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass
