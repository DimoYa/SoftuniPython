products = input().split()
products_dict = {products[i]: int(products[i + 1]) for i in range(0, len(products), 2)}
searched_products = [product for product in input().split()]

for search_product in searched_products:
    found = False
    for product in products_dict:
        if search_product in product:
            print(f"We have {products_dict[product]} of {search_product} left")
            found = True
            break
    if not found:
        print(f"Sorry, we don't have {search_product}")

