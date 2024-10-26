import math
from collections import deque

bees_queue = deque([int(el) for el in input().split()])
bee_eaters_stack = [int(el) for el in input().split()]

while bees_queue and bee_eaters_stack:
    current_bee = bees_queue.popleft()
    current_eater = bee_eaters_stack.pop()

    eater_power = current_eater * 7

    if eater_power < current_bee:
        bees_queue.append(current_bee - eater_power)
    elif current_bee > eater_power:
        bee_eaters_stack.append(math.ceil(eater_power - current_bee // 7))
    else:
        continue

print("The final battle is over!")
if not bees_queue and not bee_eaters_stack:
    print("But no one made it out alive!")
if bees_queue:
    print(f"Bee groups left: {', '.join(map(str, bees_queue))}")
if bee_eaters_stack:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_stack))}")
