products_input = input()
products = {}

while not products_input == "statistics":
    key, value = products_input.split(": ")
    value = int(value)
    if key not in products:
        products[key] = value
    else:
        products[key] += value
    products_input = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
