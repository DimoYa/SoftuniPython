def plant_garden(available_garden_space, *allowed_types, **planting_requests):
    allowed_map = dict(allowed_types)
    planted_plants = {}
    all_planted = True
    result = []

    for p_type, count in sorted(planting_requests.items()):
        if p_type in allowed_map:
            per_plant_space = allowed_map[p_type]
            required_space = count * per_plant_space

            if available_garden_space >= required_space:
                planted_plants[p_type] = count
                available_garden_space -= required_space
            elif available_garden_space >= per_plant_space:
                all_planted = False
                minimum_count = int(available_garden_space / allowed_map[p_type])
                planted_plants[p_type] = minimum_count
                available_garden_space -= minimum_count * per_plant_space
            else:
                all_planted = False

    if all_planted:
        result.append(f"All plants were planted! Available garden space: {available_garden_space} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")
    result.append("Planted plants:")

    for plant_type, piece in sorted(planted_plants.items()):
        result.append(f"{plant_type}: {piece}")

    return "\n".join(result)

print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))