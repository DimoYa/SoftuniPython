budget = int(input())
season = input()
num_fishermen = int(input())

# Prices for boat rental per season in Bulgarian Lev (BGN)
price_spring = 3000
price_summer_autumn = 4200
price_winter = 2600

# Discounts based on group size
discount_up_to_6 = 0.10
discount_7_to_11 = 0.15
discount_12_and_above = 0.25
additional_discount = 0.05

total = 0

if season == 'Spring':
    total = price_spring
elif season == 'Summer' or season == 'Autumn':
    total = price_summer_autumn
else:
    total = price_winter

if num_fishermen <= 6:
    total *= (1 - discount_up_to_6)
elif 7 <= num_fishermen <= 11:
    total *= (1 - discount_7_to_11)
else:
    total *= (1 - discount_12_and_above)

if num_fishermen % 2 == 0 and season != 'Autumn':
    total *= (1- additional_discount)

diff = f'{abs(budget - total):.2f}'

if budget >= total:
    print(f'Yes! You have {diff} leva left.')
else:
    print(f'Not enough money! You need {diff} leva.')