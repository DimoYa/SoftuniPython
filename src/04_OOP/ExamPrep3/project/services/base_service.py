from abc import ABC, abstractmethod

from project.robots.base_robot import BaseRobot


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.type = None
        self.robots: list[BaseRobot] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @abstractmethod
    def details(self):
        pass

