from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return "Extreme"
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"
        else:
            # This branch won't trigger due to BasePeak elevation validation
            return "Moderate"

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)