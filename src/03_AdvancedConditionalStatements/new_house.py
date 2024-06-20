price_rose = 5.00
price_dahlia = 3.80
price_tulip = 2.80
price_daffodil = 3.00
price_gladiolus = 2.50

flower_type = input()
quantity = int(input())
budget = int(input())


total_price = 0

if flower_type == 'Roses':
    total_price = quantity * price_rose
    if quantity > 80:
        total_price *= 0.9
elif flower_type == 'Dahlias':
    total_price = quantity * price_dahlia
    if quantity > 90:
        total_price *= 0.85
elif flower_type == 'Tulips':
    total_price = quantity * price_tulip
    if quantity > 80:
        total_price *= 0.85
elif flower_type == 'Narcissus':
    total_price = quantity * price_daffodil
    if quantity < 120:
        total_price *= 1.15
elif flower_type == 'Gladiolus':
    total_price = quantity * price_gladiolus
    if quantity < 80:
        total_price *= 1.2

diff = f'{abs(budget - total_price):.2f}'

if budget >= total_price:
    print(f'Hey, you have a great garden with {quantity} {flower_type} and {diff} leva left.')
else:
    print(f'Not enough money, you need {diff} leva more.')
