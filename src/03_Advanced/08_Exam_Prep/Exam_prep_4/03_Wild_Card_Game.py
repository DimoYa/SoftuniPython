def draw_cards(*first_group, **second_group):
    monsters = {}
    spells = {}
    result = ""

    for item in first_group:
        if item[1] == "monster":
            if item[0] not in monsters:
                monsters[item[1]] = []
            monsters[item[1]].append(item[0])
        else:
            if item[0] not in spells:
                spells[item[1]] = []
            spells[item[1]].append(item[0])

    for k, v in second_group.items():
        if v == "monster":
            if k not in monsters:
                monsters[v] = []
            monsters[v].append(k)
        else:
            if v not in spells:
                spells[v] = []
            spells[v].append(k)

    if monsters:
        result += "Monster cards:\n"
        for k, v in sorted(monsters.items(), key=lambda kvp: kvp[0], reverse=True):
            result += f"{'\n'.join({f"  ***{v}\n,"})}"

    result.rstrip()

    if spells:
        result += "Spell cards:\n"
        for k, v in sorted(spells.items(), key=lambda kvp: kvp[0]):
            result += f"  $$${v}\n,"

    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))

print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
