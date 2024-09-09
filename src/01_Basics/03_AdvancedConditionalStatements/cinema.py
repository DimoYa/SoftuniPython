price_premiere = 12.00
price_normal = 7.50
price_discount = 5.00

screening_type = input()
num_rows = int(input())
num_columns = int(input())
total = num_rows * num_columns

if screening_type == 'Premiere':
    total *= price_premiere
elif screening_type == 'Normal':
    total *= price_normal
else:
    total *= price_discount

print(f'{total:.2f} leva')
