from project.player import Player
from project.supply.supply import Supply
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    supply_types = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def add_player(self, *players: Player):
        added_players_names = []
        for pl in players:
            if pl not in self.players:
                self.players.append(pl)
                added_players_names.append(pl.name)

        return f"Successfully added: {', '.join(added_players_names)}"

    def add_supply(self, *suppliers: Supply):
        for sp in suppliers:
            self.supplies.append(sp)

    def sustain(self, player_name: str, sustenance_type: str):
        player = next((pl for pl in self.players if pl.name == player_name), None)

        if not player or sustenance_type not in self.supply_types:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply_class = Food if sustenance_type == "Food" else Drink

        # Find last supply index and remove it
        for i in range(len(self.supplies) - 1, -1, -1):
            if isinstance(self.supplies[i], supply_class):
                supply = self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(100, player.stamina + supply.energy)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = next((pl for pl in self.players if pl.name == first_player_name), None)
        second_player = next((pl for pl in self.players if pl.name == second_player_name), None)

        if first_player.stamina == 0 or second_player.stamina == 0:
            messages = []
            if first_player.stamina == 0:
                messages.append(f"Player {first_player.name} does not have enough stamina.")
            if second_player.stamina == 0:
                messages.append(f"Player {second_player.name} does not have enough stamina.")
            return "\n".join(messages)

            # Determine who attacks first (lower stamina attacks first)
        if first_player.stamina < second_player.stamina:
            attacker, defender = first_player, second_player
        else:
            attacker, defender = second_player, first_player

            # First attack
        defender.stamina -= attacker.stamina / 2
        if defender.stamina <= 0:
            defender.stamina = 0
            return f"Winner: {attacker.name}"

        # Second attack
        attacker.stamina -= defender.stamina / 2
        if attacker.stamina <= 0:
            attacker.stamina = 0
            return f"Winner: {defender.name}"

        # If both still alive, compare stamina
        if attacker.stamina > defender.stamina:
            winner = attacker
        else:
            winner = defender

        return f"Winner: {winner.name}"

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)
        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = []

        for pl in self.players:
            result.append(pl.__str__())

        for sp in self.supplies:
            result.append(sp.details())

        return "\n".join(result)