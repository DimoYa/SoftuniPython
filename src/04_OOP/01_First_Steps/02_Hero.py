class Hero:
    def __init__(self, name: str, health: int):
        self.health = health
        self.name = name

    def defend(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount: int):
        self.health += amount


hero = Hero("Alexander", 75)
print(hero.defend(20))