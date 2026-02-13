from typing import List


class Hero:
    def __init__(self, name, _hp, _mp):
        self.name = name
        self.hp = _hp
        self.mp = _mp

n = int(input())
heros: List[Hero] = []


for _ in range(n):
    hero_name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    hero = Hero(hero_name, hp, mp)
    heros.append(hero)

command = input()


def cast_spell_command(parameters):
    hero_name_param, mp_needed, spell_name = parameters
    mp_needed = int(mp_needed)
    current_hero = next((h for h in heros if h.name == hero_name_param), None)

    if current_hero.mp < mp_needed:
        return f"{hero_name_param} does not have enough MP to cast {spell_name}!"

    current_hero.mp -= mp_needed

    return f"{hero_name_param} has successfully cast {spell_name} and now has {current_hero.mp} MP!"


def take_damage_command(parameters):
    hero_name_param, damage, attacker = parameters
    damage = int(damage)

    current_hero = next((h for h in heros if h.name == hero_name_param), None)

    current_hero.hp -= damage

    if current_hero.hp <= 0:
        heros.remove(current_hero)
        return f"{hero_name_param} has been killed by {attacker}!"

    return f"{hero_name_param} was hit for {damage} HP by {attacker} and now has {current_hero.hp} HP left!"


def recharge_command(parameters):
    hero_name_param, amount = parameters
    amount = int(amount)

    current_hero = next((h for h in heros if h.name == hero_name_param), None)

    amount_to_recharge = min(amount, 200 - current_hero.mp)
    current_hero.mp += amount_to_recharge

    return f"{hero_name_param} recharged for {amount_to_recharge} MP!"


def heal_command(parameters):
    hero_name_param, amount = parameters
    amount = int(amount)

    current_hero = next((h for h in heros if h.name == hero_name_param), None)

    amount_to_heal = min(amount, 100 - current_hero.hp)
    current_hero.hp += amount_to_heal

    return f"{hero_name_param} healed for {amount_to_heal} HP!"


while command != "End":
    token = command.split(" - ")
    command_name = token[0]
    command_parameters = token[1:]

    result = None

    if command_name == "CastSpell":
        result = cast_spell_command(command_parameters)
    elif command_name == "TakeDamage":
        result = take_damage_command(command_parameters)
    elif command_name == "Recharge":
        result = recharge_command(command_parameters)
    elif command_name == "Heal":
        result = heal_command(command_parameters)

    command = input()
    print(result)

for hero in heros:
    print(f"{hero.name}\n  HP: {hero.hp}\n  MP: {hero.mp}")