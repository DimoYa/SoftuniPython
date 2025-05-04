from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    robot_types = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    service_types = {"MainService": MainService, "SecondaryService": SecondaryService}

    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    def add_service(self, s_type: str, name: str):
        if s_type not in self.service_types:
            raise Exception("Invalid service type!")

        service = self.service_types[s_type](name)
        self.services.append(service)
        return f"{s_type} is successfully added."

    def add_robot(self, r_type: str, name: str, kind: str, price: float):
        if r_type not in self.robot_types:
            raise Exception("Invalid robot type!")

        robot = self.robot_types[r_type](name, kind, price)
        self.robots.append(robot)
        return f"{r_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if (robot.type == "Female" and service.type != "Secondary") or \
                (robot.type == "Male" and service.type != "Main"):
            return "Unsuitable service."

        if service.capacity <= 0:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        service.capacity -= 1

        return f"Successfully added {robot.name} to {service.name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(s for s in self.services if s.name == service_name)

        robot = next((r for r in service.robots if r.name == robot_name), None)
        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        service.capacity += 1

        return f"Successfully removed {robot.name} from {service.name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)

        robots_fed = 0
        for robot in service.robots:
            robot.eating()
            robots_fed += 1

        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)

        sum_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {sum_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return "\n".join(result)

