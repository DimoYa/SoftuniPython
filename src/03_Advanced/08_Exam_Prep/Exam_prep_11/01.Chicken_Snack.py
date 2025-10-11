from collections import deque

amount_of_money_stack = [int(el) for el in input().split()]
prices_of_food_queue = deque([int(el) for el in input().split()])
eaten_food = 0

while amount_of_money_stack and prices_of_food_queue:
    current_money = amount_of_money_stack[-1]
    current_price = prices_of_food_queue[0]

    if current_money == current_price:
        eaten_food += 1
        amount_of_money_stack.pop()
        prices_of_food_queue.popleft()
    elif current_money > current_price:
        eaten_food += 1
        change = current_money - current_price
        prices_of_food_queue.popleft()
        amount_of_money_stack.pop()
        if not amount_of_money_stack:
            amount_of_money_stack.append(change)
        else:
            amount_of_money_stack[-1] += change
    elif current_money < current_price:
        amount_of_money_stack.pop()
        prices_of_food_queue.popleft()

result = ""

if not eaten_food:
    result = "Henry remained hungry. He will try next weekend again."
else:
    if eaten_food >= 4:
        result = f"Gluttony of the day! Henry ate {eaten_food} "
    else:
        result = f"Henry ate: {eaten_food} "
    if eaten_food > 1:
        result += "foods."
    else:
        result += "food."

print(result)
