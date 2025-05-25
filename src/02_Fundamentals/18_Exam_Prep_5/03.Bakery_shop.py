class Stock:
    def __init__(self, food: str, quantity: int):
        self.food = food
        self.quantity = quantity


def receive_command(command_parameters):
    quantity, food = command_parameters
    quantity = int(quantity)

    if quantity <= 0:
        return

    current_stock = next((s for s in bakery_shop if s.food == food), None)

    if not current_stock:
        bakery_shop.append(Stock(food, quantity))
    else:
        current_stock.quantity += quantity


def sell_command(command_parameters):
    quantity, food = command_parameters
    quantity = int(quantity)
    sold_quantity = 0

    current_stock = next((s for s in bakery_shop if s.food == food), None)

    if not current_stock:
        print(f"You do not have any {food}.")
    else:
        if quantity > current_stock.quantity:
            print(f"There aren't enough {food}. You sold the last {current_stock.quantity} of them.")
            sold_quantity = current_stock.quantity
            bakery_shop.remove(current_stock)
        else:
            print(f"You sold {quantity} {food}.")
            current_stock.quantity -= quantity
            sold_quantity = quantity
            if current_stock.quantity == 0:
                bakery_shop.remove(current_stock)

    return sold_quantity


bakery_shop: list[Stock] = []
total_sold_quantity = 0

command = input()
while command != "Complete":
    token = command.split()
    command_name = token[0]
    command_parameters = token[1:]

    if command_name == "Receive":
        receive_command(command_parameters)
    elif command_name == "Sell":
        total_sold_quantity += sell_command(command_parameters)

    command = input()

for item in bakery_shop:
    print(f"{item.food}: {item.quantity}")
print(f"All sold: {total_sold_quantity} goods")
