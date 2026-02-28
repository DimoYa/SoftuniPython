from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540
    def __init__(self, name):
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduction = round(time_to_catch * 0.3)
        self.oxygen_level = max(0, self.oxygen_level - reduction)

        if self.oxygen_level == 0:
            self.update_health_status()

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL

