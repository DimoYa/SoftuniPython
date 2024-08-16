class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

    def shoot(self):
        if not self.bullets == 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
