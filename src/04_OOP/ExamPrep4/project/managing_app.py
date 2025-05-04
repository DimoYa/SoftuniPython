from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    vehicle_types = {"CargoVan": CargoVan, "PassengerCar": PassengerCar}

    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.vehicle_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.vehicle_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = next((r for r in self.routes if r.start_point == start_point
                     and r.end_point == end_point and r.length == length), None)

        if route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        shorter_route = next((r for r in self.routes if r.start_point == start_point
                              and r.end_point == end_point and r.length < length), None)

        if shorter_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        greater_route = next((r for r in self.routes if r.start_point == start_point
                              and r.end_point == end_point and r.length > length), None)

        if greater_route:
            greater_route.is_locked = True

        route_id = len(self.routes) + 1

        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle

    def repair_vehicles(self, count: int):
        damaged = [v for v in self.vehicles if v.is_damaged]

        damaged_sorted = sorted(damaged, key=lambda v: (v.brand, v.model))

        result = damaged_sorted[:count]

        for v in result:
            v.is_damaged = False
            v.battery_level = 100

        return f"{len(result)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)

        user_info = "\n".join(str(user) for user in sorted_users)

        return f"*** E-Drive-Rent ***\n{user_info}"
