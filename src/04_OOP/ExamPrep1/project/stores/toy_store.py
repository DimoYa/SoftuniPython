from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)
        self.sell = "Toys"

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        result = (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                  f"{self.get_estimated_profit()}\n")

        result += "**Toys for sale:\n"

        details = {}

        for model in sorted(details):
            stats = details[model]
            avg_price = stats["total_price"] / stats["count"]
            result += f"{model}: {stats['count']}pcs, average price: {avg_price:.2f}\n"
        return result[:-1]

        for model in sorted(details):
            stats = details[model]
            result += f"{model}: {stats['count']}pcs, average price: {(stats['total_price'] / stats['count']):.2f}"

        return result[:-1]
