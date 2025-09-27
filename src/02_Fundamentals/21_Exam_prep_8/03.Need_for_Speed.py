from typing import List

class Car:
    def __init__(self, name, ml, fl):
        self.name = name
        self.ml = ml
        self.fl = fl

n = int(input())
cars: List[Car] = []

for _ in range(n):
    car_name, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    car = Car(car_name, mileage, fuel)
    cars.append(car)

command = input()

def drive_command(command_params):
    car_name_param, distance, fuel_param = command_params
    distance = int(distance)
    fuel_param = int(fuel_param)

    current_car = next((c for c in cars if c.name == car_name_param), None)

    if current_car.fl < fuel_param:
        return "Not enough fuel to make that ride"

    current_car.ml += distance
    current_car.fl -= fuel_param

    result_to_return = f"{car_name_param} driven for {distance} kilometers. {fuel_param} liters of fuel consumed."

    if current_car.ml >= 100000:
        cars.remove(current_car)
        result_to_return += f"\nTime to sell the {car_name_param}!"

    return result_to_return


def refuel_command(command_params):
    car_name_param, fuel_param = command_params
    fuel_param = int(fuel_param)

    current_car = next((c for c in cars if c.name == car_name_param), None)
    if current_car is None:
        return None

    available_space = 75 - current_car.fl
    fuel_to_refueled = min(available_space, fuel_param)

    current_car.fl += fuel_to_refueled
    return f"{car_name_param} refueled with {fuel_to_refueled} liters"

def revert_command(command_params):
    car_name_param, km_params = command_params
    km_params = int(km_params)

    current_car = next((c for c in cars if c.name == car_name_param), None)

    old_mileage = current_car.ml
    current_car.ml -= km_params

    if current_car.ml < 10000:
        current_car.ml = 10000
        return None

    actual_decreased = old_mileage - current_car.ml
    return f"{car_name_param} mileage decreased by {actual_decreased} kilometers"

while command != "Stop":
    token = command.split(" : ")
    command_name = token[0]
    command_parameters = token[1:]

    result = None
    if command_name == "Drive":
        result = drive_command(command_parameters)
    elif command_name == "Refuel":
        result = refuel_command(command_parameters)
    elif command_name == "Revert":
        result = revert_command(command_parameters)

    if result is not None:
        print(result)

    command = input()

for car in cars:
    print(f"{car.name} -> Mileage: {car.ml} kms, Fuel in the tank: {car.fl} lt.")
