def team_lineup(*args):
    players = {}
    result = ""

    for player, country in args:
        if country not in players:
            players[country] = []
        players[country].append(player)

    for country, player in sorted(players.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f"{country}:\n"
        result += '\n'.join(f"  -{p}" for p in player)
        result += '\n'

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
