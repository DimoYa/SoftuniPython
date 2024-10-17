def cookbook(*args):
    cuisine_dict = {}
    result = ""
    for arg in args:
        name, cuisine, ingredients = arg

        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append({
            "name": name,
            "ingredients": ingredients
        })

    for k, v in sorted(cuisine_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f"{k} cuisine contains {len(v)} recipes:\n"
        for item in sorted(v, key=lambda x: x['name']):
            result += f"  * {item['name']} -> Ingredients: {', '.join(item['ingredients'])}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
