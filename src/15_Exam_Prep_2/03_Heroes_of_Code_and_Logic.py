class Hero:
    def __init__(self, name, hit_points, mana_points):
        self.name = name
        self.hp = min(hit_points, 100)
        self.mp = min(mana_points, 200)


integer = int(input())
heroes = {}

for _ in range(integer):
    hero_name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    hero = Hero(hero_name, hp, mp)
    heroes[hero_name] = hero

command = input()


def cast_spell_command(heroes_dict, commands):
    name = commands[0]
    mp_needed = int(commands[1])
    spell_name = commands[2]

    current_hero = heroes_dict[name]

    if current_hero.mp >= mp_needed:
        current_hero.mp -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {current_hero.mp} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")

    return heroes_dict


def take_damage_command(heroes_dict, commands):
    name = commands[0]
    damage = int(commands[1])
    attacker = commands[2]
    current_hero = heroes_dict[name]

    current_hero.hp -= damage

    if current_hero.hp > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {current_hero.hp} HP left!")
    else:
        del heroes_dict[name]
        print(f"{name} has been killed by {attacker}!")

    return heroes_dict


def recharge_command(heroes_dict, commands):
    name = commands[0]
    amount = int(commands[1])
    current_hero = heroes_dict[name]
    recovered_amount = min(amount, (200 - current_hero.mp))

    current_hero.mp += recovered_amount
    print(f"{name} recharged for {recovered_amount} MP!")
    return heroes_dict


def heal_command(heroes_dict, commands):
    name = commands[0]
    amount = int(commands[1])
    current_hero = heroes_dict[name]
    recovered_amount = min(amount, (100 - current_hero.hp))

    current_hero.hp += recovered_amount
    print(f"{name} healed for {recovered_amount} HP!")
    return heroes_dict


while not command == "End":
    token = command.split(" - ")
    command_name = token[0]
    command_params = token[1:]

    if command_name == "CastSpell":
        heroes = cast_spell_command(heroes, command_params)
    elif command_name == "TakeDamage":
        heroes = take_damage_command(heroes, command_params)
    elif command_name == "Recharge":
        heroes = recharge_command(heroes, command_params)
    elif command_name == "Heal":
        heroes = heal_command(heroes, command_params)

    command = input()

for key, value in heroes.items():
    print(key)
    print(f"  HP: {value.hp}")
    print(f"  MP: {value.mp}")
