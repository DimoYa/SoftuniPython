n = int(input())

even_set = set()
odd_set = set()

for index in range(1, n + 1):
    name = input()
    asci_value = 0

    for i in range(len(name)):
        asci_value += ord(name[i])

    current_result = int(asci_value / index)

    if current_result % 2 == 0:
        even_set.add(current_result)
    else:
        odd_set.add(current_result)

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)
result = ""

if sum_odd_set == sum_even_set:
    result = odd_set.union(even_set)
elif sum_odd_set > sum_even_set:
    result = odd_set.difference(even_set)
elif sum_even_set > sum_odd_set:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=', ')
