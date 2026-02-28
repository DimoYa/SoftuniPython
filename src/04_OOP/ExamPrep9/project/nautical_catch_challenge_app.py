from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish

class NauticalCatchChallengeApp:
    divers_types = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    fish_types = {"DeepSeaFish": DeepSeaFish, "PredatoryFish": PredatoryFish}

    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.divers_types:
            return f"{diver_type} is not allowed in our competition."

        diver = next((d for d in self.divers if d.name == diver_name), None)

        if diver:
            return f"{diver_name} is already a participant."

        diver = self.divers_types[diver_type](diver_name)

        self.divers.append(diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.fish_types:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)

        if fish:
            return f"{fish_name} is already permitted."

        fish = self.fish_types[fish_type](fish_name, points)

        self.fish_list.append(fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        # CASE 1: oxygen less → DO NOTHING except message
        if diver.oxygen_level < fish.time_to_catch:
            return f"{diver_name} missed a good {fish_name}."

        # CASE 2: oxygen equal
        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        # CASE 3: oxygen greater
        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for d in self.divers:
            if d.has_health_issue:
                d.update_health_status()
                d.oxygen_level = d.INITIAL_OXYGEN_LEVEL
                count +=1

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)

        result = f"**{diver_name} Catch Report**"

        for f in diver.catch:
            result += f"\n{f.fish_details()}"
        return result


    def competition_statistics(self):
        divers = [d for d in self.divers if not d.has_health_issue]

        divers.sort(key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        result = f"**Nautical Catch Challenge Statistics**"

        for d in divers:
            result += f"\n{d}"
        return result