def cookbook(*recipes):
    book = {}

    for recipe in recipes:
        recipe_name, cuisine, ingredients = recipe
        if cuisine not in book:
            book[cuisine] = []
        book[cuisine].append({
            "name": recipe_name,
            "ingredients": ingredients
        })

    # Sort recipes alphabetically by name within each cuisine
    for cuisine in book:
        book[cuisine] = sorted(book[cuisine], key=lambda r: r["name"])

    # Sort cuisines by number of recipes (descending), then alphabetically
    sorted_book = dict(
        sorted(book.items(), key=lambda x: (-len(x[1]), x[0]))
    )

    # Format the output
    result_lines = []
    for cuisine, recipes_list in sorted_book.items():
        result_lines.append(f"{cuisine} cuisine contains {len(recipes_list)} recipes:")
        for recipe in recipes_list:
            ingredients_str = ", ".join(recipe["ingredients"])
            result_lines.append(f"  * {recipe['name']} -> Ingredients: {ingredients_str}")

    return "\n".join(result_lines)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
