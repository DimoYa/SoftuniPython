def boarding_passengers(ship_capacity, *args):
    boarded = {}
    total_passengers = sum(group[0] for group in args)
    result = ""

    for cap, cat in args:
        if ship_capacity - cap >= 0:
            if cat not in boarded:
                boarded[cat] = 0
            boarded[cat] += cap
            ship_capacity -= cap
            total_passengers -= cap

    result += "Boarding details by benefit plan:\n"
    for cat, cap in sorted(boarded.items(), key=lambda x: (-x[1], x[0])):
        result += f"## {cat}: {cap} guests\n"

    if ship_capacity != 0 and total_passengers != 0:
        result += f"Partial boarding completed. Available capacity: {ship_capacity}."
    elif ship_capacity == 0 and total_passengers != 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += "All passengers are successfully boarded!"

    return result


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
