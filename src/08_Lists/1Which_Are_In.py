first_line = input().split(', ')
second_line = input().split(', ')

result = []

for s1 in first_line:
    for s2 in second_line:
        if s1 in s2:
            result.append(s1)
            break

print(result)
