n = int(input())
total_price = 0

for _ in range(n):
    price_per_capsula = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsula <= 100.00 and 1<= days <= 31 and  1 <= capsules_per_day <= 2000:
        current_price = price_per_capsula * days * capsules_per_day
        total_price += current_price
        print(f'The price for the coffee is: ${current_price:.2f}')

print(f'Total: ${total_price:.2f}')
