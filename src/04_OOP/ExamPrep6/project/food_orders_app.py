from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    meal_types = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: list[Meal] = []
        self.clients_list: list[Client] = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

        if client:
            return f"The client has already been registered!"

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.meal_types:
                self.menu.append(meal)


    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return '\n'.join(meal.details() for meal in self.menu)


    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            meal = next((m for m in self.menu if m.name == meal_name), None)

            if meal is None:
                raise Exception(f"{meal_name} is not on the menu!")
            if meal_quantity > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

            meal_price = meal.price
            meal_class = self.meal_types[meal.__class__.__name__]
            current_meal = meal_class(meal.name, meal.price, meal_quantity)
            client.shopping_cart.append(current_meal)

            client.bill += meal_price * meal_quantity
            meal.quantity -= meal_quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(c.name for c in client.shopping_cart)} for {client.bill:.2f}lv."


    def cancel_order(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            current_item = next((m for m in self.menu if m.name == meal.name), None)
            if current_item:
                current_item.quantity += meal.quantity

        client.shopping_cart.clear()
        client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        total_paid_money = client.bill

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.shopping_cart.clear()
        client.bill = 0.0
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."