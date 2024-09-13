n, m = [int(num) for num in input().split()]

first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(int(input()))

for _ in range(m):
    second_set.add(int(input()))

result = first_set.intersection(second_set)

print(*result, sep='\n')
