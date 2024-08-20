class Beer:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

line = input()
beer_dict = {}

while line != "buy":
    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in beer_dict:
        beer_dict[name] = Beer(price, quantity)
    else:
        beer_dict[name].quantity += quantity
        beer_dict[name].price = price  # Update price to the most recent one

    line = input()

for key, value in beer_dict.items():
    total_price = value.quantity * value.price
    print(f"{key} -> {total_price:.2f}")
