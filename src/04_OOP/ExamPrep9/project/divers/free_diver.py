from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120
    def __init__(self, name):
        super().__init__(name, FreeDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduction = round(time_to_catch * 0.6)
        self.oxygen_level = max(0, self.oxygen_level - reduction)

        if self.oxygen_level == 0:
            self.update_health_status()

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL

