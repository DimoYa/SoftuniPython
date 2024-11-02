from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: [Product] = []

    def add(self, product: Product):
        if product not in self.products:
            self.products.append(product)

    def find(self, product_name: str):
        try:
            product = [p for p in self.products if p.name == product_name][0]
            return product
        except IndexError:
            pass

    def remove(self, product_name: str):
        try:
           product = [p for p in self.products if p.name == product_name][0]
           self.products.remove(product)
        except IndexError:
           pass

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
