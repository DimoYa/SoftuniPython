# Read input from console
N1 = int(input())
N2 = int(input())
operator = input()

output = ''

if operator == '+':
    result = N1 + N2
    even_or_odd = 'even' if result % 2 == 0 else 'odd'
    output = f'{N1} {operator} {N2} = {result} - {even_or_odd}'
elif operator == '-':
    result = N1 - N2
    even_or_odd = 'even' if result % 2 == 0 else 'odd'
    output = f'{N1} {operator} {N2} = {result} - {even_or_odd}'
elif operator == '*':
    result = N1 * N2
    even_or_odd = 'even' if result % 2 == 0 else 'odd'
    output = f'{N1} {operator} {N2} = {result} - {even_or_odd}'
elif operator == '/':
    if N2 != 0:
        result = N1 / N2
        output = f'{N1} {operator} {N2} = {result:.2f}'
    else:
        output = f'Cannot divide {N1} by zero'
elif operator == '%':
    if N2 != 0:
        result = N1 % N2
        output = f'{N1} {operator} {N2} = {result}'
    else:
        output = f'Cannot divide {N1} by zero'
else:
    print('Invalid operator entered. Please use one of the following: +, -, *, /, %.')

print(output)
