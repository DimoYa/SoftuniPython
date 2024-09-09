food = input().split()
food_dict = {food[i]: int(food[i + 1]) for i in range(0, len(food), 2)}

print(food_dict)
