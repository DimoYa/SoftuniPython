from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    CHAIR_MATERIAL = "Wood"
    CHAIR_SUBTYPE = "Furniture"

    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.CHAIR_MATERIAL, self.CHAIR_SUBTYPE)

    def discount(self):
        self.price *= 0.9
