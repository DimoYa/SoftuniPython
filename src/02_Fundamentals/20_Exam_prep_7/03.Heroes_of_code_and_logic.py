from typing import List


class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = min(hp, 100)
        self.mp = min(mp, 200)

n = int(input())
heroes: List[Hero] = []

for _ in range(n):
    hero_name, hit_points, mana_points = input().split()
    hit_points = int(hit_points)
    mana_points = int(mana_points)
    hero = Hero(hero_name, hit_points, mana_points)
    heroes.append(hero)

command = input()


def cast_spell_command(parameters):
    hero_name, mp_needed, spell_name = parameters
    mp_needed = int(mp_needed)

    current_hero = next((h for h in heroes if h.name == hero_name), None)

    if current_hero.mp < mp_needed:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        return

    current_hero.mp -= mp_needed
    print(f"{hero_name} has successfully cast {spell_name} and now has {current_hero.mp} MP!")


def take_damage_command(parameters):
    hero_name, damage, attacker = parameters
    damage = int(damage)

    current_hero = next((h for h in heroes if h.name == hero_name), None)
    current_hero.hp -= damage

    if current_hero.hp <= 0:
        print(f"{hero_name} has been killed by {attacker}!")
        heroes.remove(current_hero)
        return

    print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hero.hp} HP left!")


def recharge_command(parameters):
    hero_name, amount = parameters
    amount = int(amount)

    current_hero = next((h for h in heroes if h.name == hero_name), None)
    before = current_hero.mp
    current_hero.mp = min(current_hero.mp + amount, 200)
    recovered = current_hero.mp - before

    print(f"{hero_name} recharged for {recovered} MP!")


def heal_command(parameters):
    hero_name, amount = parameters
    amount = int(amount)

    current_hero = next((h for h in heroes if h.name == hero_name), None)
    before = current_hero.hp
    current_hero.hp = min(current_hero.hp + amount, 100)
    recovered = current_hero.hp - before

    print(f"{hero_name} healed for {recovered} HP!")


while not command == "End":
    token = command.split(" - ")
    command_name = token[0]
    command_parameters = token[1:]

    if command_name == "CastSpell":
        cast_spell_command(command_parameters)
    elif command_name == "TakeDamage":
        take_damage_command(command_parameters)
    elif command_name == "Recharge":
        recharge_command(command_parameters)
    elif command_name == "Heal":
        heal_command(command_parameters)

    command = input()

for hero in heroes:
    print(hero.name)
    print(f"  HP: {hero.hp}")
    print(f"  MP: {hero.mp}")
