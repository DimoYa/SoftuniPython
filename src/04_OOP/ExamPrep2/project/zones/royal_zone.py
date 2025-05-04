from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, 10)
        self.type = "Royal"

    def zone_info(self):
        royal_count = len([p for p in self.ships if p.type == "Pirates"])
        result = "@Royal Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += (f"Battleships currently in the Royal Zone: {len(self.ships)}, {royal_count} "
                   f"out of them are Pirate Battleships.\n")

        sorted_ships = self.get_ships()
        if sorted_ships:
            result += "#"
            ship_names = ", ".join(f"{ship.name}" for ship in sorted_ships)
            result += ship_names
            result += "#"
        else:
            result = result.rstrip()

        return result

