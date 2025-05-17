import re

line = input()
pattern = r"([#|])(?P<item_name>[A-Za-z\s]+)\1(?P<exp_date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>(0|[1-9][0-9]{0,3}|10000))\1"
matches = re.finditer(pattern, line)
calories_per_day = 2000
items = []
total_calories = 0

food_info = [math.groupdict() for math in matches]

for food in food_info:
    items.append(f"Item: {food['item_name']}, Best before: {food['exp_date']}, Nutrition: {food['calories']}")
    total_calories += int(food['calories'])

days_to_keep = int(total_calories / calories_per_day)

print(f"You have food to last you for: {days_to_keep} days!")
print("\n".join(items), end="")