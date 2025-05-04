from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    def __init__(self, name):
        super().__init__(name, 15000, 2000)

    def increase_money(self):
        self.available_money += 1000

