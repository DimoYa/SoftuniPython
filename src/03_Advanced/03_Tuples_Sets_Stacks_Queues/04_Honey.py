import operator
from collections import deque

bees = deque([int(num) for num in input().split()])
nectar = [int(num) for num in input().split()]
symbols = deque(input().split())
honey_made = 0

operation_mapper = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

while bees and nectar:

    current_bee = bees[0]
    current_nectar = nectar[-1]

    if current_bee > current_nectar:
        nectar.pop()
        continue
    else:
        nectar.pop()
        bees.popleft()
        if symbols[0] == "/" and current_nectar == 0:
            symbols.popleft()
            continue
        else:
            honey_made += abs(operation_mapper[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(item) for item in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(item) for item in nectar])}")