from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    def eating(self):
        self.weight += 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 9)
        self.type = "Male"
