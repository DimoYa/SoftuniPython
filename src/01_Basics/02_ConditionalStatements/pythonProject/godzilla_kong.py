budget_for_movie = float(input())
num_extras = int(input())
cost_per_outfit = float(input())

decor_cost = budget_for_movie * 0.1
clothes_cost = num_extras * cost_per_outfit

if num_extras > 150:
    clothes_cost *= 0.9

total = decor_cost + clothes_cost
diff = abs(budget_for_movie - total)

if total > budget_for_movie:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
