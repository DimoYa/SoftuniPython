def extinguishing_the_fire(water, current_value_of_fire, total_fire, total_effort, cells):
    if water >= current_value_of_fire:
        water -= current_value_of_fire
        total_fire += current_value_of_fire
        total_effort += 0.25 * current_value_of_fire
        cells.append(current_value_of_fire)
    return water, total_fire, total_effort, cells


fires = input().split('#')
water = int(input())
cells = []
total_fire = 0
total_effort = 0


for fire_item in fires:
    split_item = fire_item.split(" = ")
    current_type_of_cell = split_item[0]
    current_value_of_fire = int(split_item[1])


    if current_type_of_cell == "High":
        if 81 <= current_value_of_fire <= 125:
            water, total_fire, total_effort, cells = extinguishing_the_fire(water, current_value_of_fire, total_fire, total_effort, cells)
    elif current_type_of_cell == "Medium":
        if 51 <= current_value_of_fire <= 80:
            water, total_fire, total_effort, cells = extinguishing_the_fire(water, current_value_of_fire, total_fire, total_effort, cells)
    else:
        if 1 <= current_value_of_fire <= 50:
            water, total_fire, total_effort, cells = extinguishing_the_fire(water, current_value_of_fire, total_fire, total_effort, cells)

print("Cells:")
for item in cells:
    print(f"- {item}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
