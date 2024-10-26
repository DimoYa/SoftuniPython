class Pokemon:
    def __init__(self, name: str, health: int):
        self.health = health
        self.name = name

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"
