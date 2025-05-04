from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, 8)
        self.type = "Pirates"

    def zone_info(self):
        pirates_count = len([p for p in self.ships if p.type == "Royal"])
        result = "@Pirate Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += (f"Battleships currently in the Pirate Zone: {len(self.ships)}, {pirates_count} "
                   f"out of them are Royal Battleships.\n")

        sorted_ships = self.get_ships()
        if sorted_ships:
            result += "#"
            ship_names = ", ".join(f"{ship.name}" for ship in sorted_ships)
            result += ship_names
            result += "#"
        else:
            result = result.rstrip()

        return result
