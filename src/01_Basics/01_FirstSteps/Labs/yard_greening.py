square_meters = float(input())

price_per_square_meter = 7.61
sum_value = square_meters * price_per_square_meter
discount = sum_value * 0.18


print(f'The final price is: {sum_value - discount} lv.')
print(f'The discount is: {discount} lv.')
