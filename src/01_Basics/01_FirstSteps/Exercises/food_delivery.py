chicken_meal = 10.35
fish_meal = 12.40
vegetarian_meal = 8.15

chicken_count = int(input())
fish_count = int(input())
vegetarian_count = int(input())

price_for_delivery = 2.50
price_for_desert_per = 0.20

total_chicken = chicken_meal * chicken_count
total_fish = fish_meal * fish_count
total_vegetarian = vegetarian_meal * vegetarian_count

total = total_chicken + total_fish + total_vegetarian

total_amount = total + price_for_delivery + total * price_for_desert_per
print(total_amount)
