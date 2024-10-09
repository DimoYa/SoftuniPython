from collections import deque

bees_queue = deque([int(el) for el in input().split()])
bee_eaters_stack = [int(el) for el in input().split()]

while bees_queue and bee_eaters_stack:
    current_bee = bees_queue[0]
    current_eater = bee_eaters_stack[-1]

    print()