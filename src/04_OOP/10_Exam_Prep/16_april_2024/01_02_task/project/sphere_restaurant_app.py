from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    waiters_types = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    clients_types = {"RegularClient": RegularClient, "VIPClient": VIPClient}
    waiters: list[BaseWaiter] = []
    clients: list[BaseClient] = []

    # def __init__(self):

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.waiters_types:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = next((w for w in self.waiters if w.name == waiter_name), None)

        if waiter:
            return f"{waiter_name} is already on the staff."

        waiter = self.waiters_types[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)

        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.clients_types:
            return f"{client_type} is not a recognized client type."

        client = next((c for c in self.clients if c.name == client_name), None)

        if client:
            return f"{client_name} is already a client."

        client = self.clients_types[client_type](client_name)
        self.clients.append(client)

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)

        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = next((c for c in self.clients if c.name == client_name), None)

        if not client:
            return f"{client_name} is not a registered client."

        earned_points = client.earning_points(order_amount)

        return f"{client_name} earned {earned_points} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = next((c for c in self.clients if c.name == client_name), None)

        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        client.points = remaining_points
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    @staticmethod
    def generate_report():
        total_earnings = 0.0
        waiter_earnings = []

        for waiter in SphereRestaurantApp.waiters:
            waiter_earning = waiter.calculate_earnings()
            total_earnings += waiter_earning
            waiter_earnings.append((waiter, waiter_earning))

        # Sort waiters by earnings in descending order
        waiter_earnings.sort(key=lambda x: x[1], reverse=True)

        # Calculate total clients unused points and count
        total_client_points = sum(client.points for client in SphereRestaurantApp.clients)
        clients_count = len(SphereRestaurantApp.clients)

        # Format the report
        report = "$$ Monthly Report $$\n"
        report += f"Total Earnings: ${total_earnings:.2f}\n"
        report += f"Total Clients Unused Points: {total_client_points}\n"
        report += f"Total Clients Count: {clients_count}\n"
        report += "** Waiter Details **\n"

        # Add waiter details
        for waiter, earning in waiter_earnings:
            report += f"Name: {waiter.name}, Total earnings: ${earning:.2f}\n"

        return report.rstrip()  # Remove trailing newline
