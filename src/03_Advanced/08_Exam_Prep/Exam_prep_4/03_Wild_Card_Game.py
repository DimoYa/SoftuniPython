def draw_cards(*first_group, **second_group):
    monsters = []
    spells = []
    result = ""

    # Process the first group of tuples
    for item in first_group:
        card_name, card_type = item
        if card_type == "monster":
            monsters.append(card_name)
        elif card_type == "spell":
            spells.append(card_name)

    # Process the second group of keyword arguments
    for card_name, card_type in second_group.items():
        if card_type == "monster":
            monsters.append(card_name)
        elif card_type == "spell":
            spells.append(card_name)

    # Sort the monster cards in descending order
    monsters.sort(reverse=True)

    # Sort the spell cards in ascending order
    spells.sort()

    # Format the result string
    if monsters:
        result += "Monster cards:\n"
        result += ''.join([f"  ***{monster}\n" for monster in monsters])

    if spells:
        if result:
            result = result.rstrip() + "\n"  # Remove trailing newline and add a new one before spell cards
        result += "Spell cards:\n"
        result += ''.join([f"  $$${spell}\n" for spell in spells])

    return result

# Test cases
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell"))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell"))
