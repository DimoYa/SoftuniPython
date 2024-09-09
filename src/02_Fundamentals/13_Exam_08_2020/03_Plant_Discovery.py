class Plant:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.rating = []


def add_rating(plant, rating):
    plant.rating.append(rating)


def update_rarity(plant, new_rarity):
    plant.rarity = new_rarity


def reset_ratings(plant):
    plant.rating.clear()


def average_rating(plant):
    return sum(plant.rating) / len(plant.rating) if plant.rating else 0.00


number = int(input())
plants = {}

for _ in range(number):
    plant_name, plant_rarity = input().split("<->")
    plant_rarity = int(plant_rarity)
    plant = Plant(plant_name, plant_rarity)

    if plant_name in plants:
        update_rarity(plants[plant_name], plant_rarity)
    else:
        plants[plant_name] = plant

command_input = input()

while not command_input == "Exhibition":
    command_parts = command_input.split(": ")
    command_name = command_parts[0]
    command_parameters = command_parts[1]

    if command_name == "Rate":
        plant_name, rating_str = command_parameters.split(" - ")
        rating = float(rating_str)
        if plant_name in plants:
            add_rating(plants[plant_name], rating)
        else:
            print("error")

    elif command_name == "Update":
        plant_name, rarity_str = command_parameters.split(" - ")
        new_rarity = int(rarity_str)
        if plant_name in plants:
            update_rarity(plants[plant_name], new_rarity)
        else:
            print("error")

    elif command_name == "Reset":
        if command_parameters in plants:
            reset_ratings(plants[command_parameters])
        else:
            print("error")

    command_input = input()

print("Plants for the exhibition:")
for plant in plants.values():
    print(f"- {plant.name}; Rarity: {plant.rarity}; Rating: {average_rating(plant):.2f}")
