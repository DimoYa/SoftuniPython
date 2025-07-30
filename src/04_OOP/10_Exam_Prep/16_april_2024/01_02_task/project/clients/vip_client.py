from project.clients.base_client import BaseClient
MEMBERSHIP_TYPE = "VIP"

class VIPClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float):
        earned = int(order_amount // 5)
        self.points += earned
        return earned