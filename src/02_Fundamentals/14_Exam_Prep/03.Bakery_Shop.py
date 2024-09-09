line = input()
food_dict = {}
sold_items = 0


def receive_command(dict_param, quantity_param, food_param):
    if quantity_param > 0:
        if food_param not in dict_param:
            dict_param[food_param] = 0
        dict_param[food_param] += quantity_param
    return dict_param


def sell_command(dict_param, quantity_param, food_param, sold_items_param):
    if food_param not in dict_param:
        print(f"You do not have any {food_param}.")
        return dict_param, sold_items_param
    if quantity_param > dict_param[food_param]:
        available = dict_param[food_param]
        sold_items_param += available
        del dict_param[food_param]
        print(f"There aren't enough {food_param}. You sold the last {available} of them.")
        return dict_param, sold_items_param
    dict_param[food_param] -= quantity_param
    sold_items_param += quantity_param
    print(f"You sold {quantity_param} {food_param}.")
    if dict_param[food_param] == 0:
        del dict_param[food_param]

    return dict_param, sold_items_param


while not line == "Complete":
    command, quantity, food = line.split()
    quantity = int(quantity)

    if command == "Receive":
        food_dict = receive_command(food_dict, quantity, food)
    elif command == "Sell":
        food_dict, sold_items = sell_command(food_dict, quantity, food, sold_items)

    line = input()

for key, value in food_dict.items():
    print(f"{key}: {value}")

print(f"All sold: {sold_items} goods")