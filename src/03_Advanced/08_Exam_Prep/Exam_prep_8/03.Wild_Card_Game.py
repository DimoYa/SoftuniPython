def draw_cards(*args, **kwargs):
    spell_cards = []
    monster_cards = []
    result = ""

    for name, type_ in args:
        if type_ == "monster":
            monster_cards.append(name)
        elif type_ == "spell":
            spell_cards.append(name)

    for name, type_ in kwargs.items():
        if type_ == "monster":
            monster_cards.append(name)
        elif type_ == "spell":
            spell_cards.append(name)

    if monster_cards:
        result = "Monster cards:\n"
        for name in sorted(monster_cards, reverse=True):
            result += f"  ***{name}\n"
    if spell_cards:
        result += "Spell cards:\n"
        for name in sorted(spell_cards):
            result += f"  $$${name}\n"

    return result.strip()


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print("----------")
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print("----------")
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))