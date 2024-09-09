type_of_drink = input()
sugar = input()
count_of_drinks = int(input())

price = 0


if type_of_drink == 'Espresso':
    if sugar == 'Without':
        price = 0.9
    elif sugar == 'Normal':
        price = 1
    else:
        price = 1.2
elif type_of_drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.2
    else:
        price = 1.6
elif type_of_drink == 'Tea':
    if sugar == 'Without':
        price = 0.5
    elif sugar == 'Normal':
        price = 0.6
    else:
        price = 0.7

price = price * count_of_drinks

if sugar == 'Without':
    price *= (1 - 0.35)

if type_of_drink == 'Espresso' and count_of_drinks >= 5:
    price *= (1 - 0.25)
if price > 15:
    price *= (1 - 0.20)

print(f'You bought {count_of_drinks} cups of {type_of_drink} for {price:.2f} lv.')