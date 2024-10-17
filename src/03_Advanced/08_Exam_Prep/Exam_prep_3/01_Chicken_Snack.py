from collections import deque

amount_of_money = [int(el) for el in input().split()]
prices_of_foods = deque([int(el) for el in input().split()])
eaten_food = 0

while amount_of_money and prices_of_foods:

    current_money = amount_of_money.pop()
    current_price = prices_of_foods.popleft()

    if current_money < current_price:
        continue

    if current_money > current_price:
        diff = current_money - current_price
        if amount_of_money:
            amount_of_money[-1] += diff
        else:
            amount_of_money.append(diff)

    eaten_food += 1

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif 0 < eaten_food < 4:
    is_plural = "food" if eaten_food == 1 else "foods"
    print(f"Henry ate: {eaten_food} {is_plural}.")
else:
    print("Henry remained hungry. He will try next weekend again.")