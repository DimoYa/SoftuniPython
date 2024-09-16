from collections import deque

chocolate_stack = [int(num) for num in input().split(", ")]
milk_queue = deque([int(num) for num in input().split(", ")])
milkshakes = 0

while chocolate_stack and milk_queue and milkshakes < 5:

    current_choco = chocolate_stack[-1]
    current_milk = milk_queue[0]

    if current_choco <= 0:
        chocolate_stack.pop()
        continue

    if current_milk <= 0:
        milk_queue.popleft()
        continue

    if current_choco == current_milk:
        chocolate_stack.pop()
        milk_queue.popleft()
        milkshakes += 1
    else:
        milk_queue.popleft()
        milk_queue.append(current_milk)
        chocolate_stack.pop()
        chocolate_stack.append(current_choco - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate_stack:
    print(f"Chocolate: {', '.join([str(item) for item in chocolate_stack])}")
else:
    print("Chocolate: empty")
if milk_queue:
    print(f"Milk: {', '.join([str(item) for item in milk_queue])}")
else:
    print("Milk: empty")
