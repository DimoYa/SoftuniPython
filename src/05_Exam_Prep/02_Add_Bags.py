minutes_per_day = int(input())
count_of_walks = int(input())
calories_per_day = int(input())

time_of_walk = minutes_per_day * count_of_walks
burnt_calories = time_of_walk * 5

half_calories = calories_per_day * 0.5

if burnt_calories >= half_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.')
