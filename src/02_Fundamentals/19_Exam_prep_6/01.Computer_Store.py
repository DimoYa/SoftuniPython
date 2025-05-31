command = input()
total_price = 0
is_special = False

while command not in ["special", "regular"]:
    prices = float(command)
    if prices <= 0:
        print("Invalid price!")
        command = input()
        if command == "special":
            is_special = True
        continue

    total_price += prices
    command = input()

    if command == "special":
        is_special = True

if  total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {total_price*0.2:.2f}$")
    print("-----------")
    final_price = total_price*1.2
    if is_special:
        final_price*=0.9
    print(f"Total price: {final_price:.2f}$")