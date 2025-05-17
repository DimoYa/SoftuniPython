from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    Hobby_MATERIAL = "Wood/Plastic"
    Hobby_SUBTYPE = "Toys"

    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.Hobby_MATERIAL, self.Hobby_SUBTYPE)

    def discount(self):
        self.price *= 0.8
