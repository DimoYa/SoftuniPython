from project.player import Player


class Guild:
    def __init__(self, name):
        self.name: str = name
        self.players: list[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."
        else:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            player = [p for p in self.players if p.name == player_name][0]
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = ""
        result += f"Guild: {self.name}\n"
        for p in self.players:
            result += p.player_info()

        return result.strip()

