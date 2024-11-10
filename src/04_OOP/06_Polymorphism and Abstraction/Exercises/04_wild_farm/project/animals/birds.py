from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def weight_increment(self):
        return 0.25

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


# Hen (Bird)
class Hen(Bird):
    @property
    def weight_increment(self):
        return 0.35

    @property
    def allowed_food(self):
        return [Vegetable, Fruit, Meat, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"