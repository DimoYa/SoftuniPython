from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    climber_types = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    peak_types = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.climber_types:
           return f"{climber_type} doesn't exist in our register."

        climber = next((c for c in self.climbers if c.name == climber_name), None)

        if climber:
            return f"{climber_name} has been already registered."

        climber= self.climber_types[climber_type](climber_name)

        self.climbers.append(climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.peak_types:
            return f"{peak_type} is an unknown type of peak."

        peak = self.peak_types[peak_type](peak_name, peak_elevation)

        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list[str]):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        peak = next((p for p in self.peaks if p.name == peak_name), None)

        missing_gears = [g for g in peak.get_recommended_gear() if g not in gear]

        if not missing_gears:
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gears))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = next((p for p in self.peaks if p.name == peak_name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if climber.can_climb():
            climber.climb(peak)
            if peak.name not in climber.conquered_peaks:
                climber.conquered_peaks.append(peak.name)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers = [c for c in self.climbers if len(c.conquered_peaks) > 0]
        conquered_peaks = {peak for climber in climbers for peak in climber.conquered_peaks}

        total_climbed_peaks = len(conquered_peaks)

        for c in climbers:
            c.conquered_peaks.sort()

        climbers.sort(key=lambda c: (-len(c.conquered_peaks), c.name))

        result = f"Total climbed peaks: {total_climbed_peaks}\n"
        result += "**Climber's statistics:**"

        for c in climbers:
            result += f"\n{c}"
        return result
