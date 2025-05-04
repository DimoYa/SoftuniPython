from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)
        self.type = "Secondary"

    def details(self):
        result = f"{self.name} Secondary Service:\n"
        result += f"Robots: "
        result += " ".join([r.name for r in self.robots]) if self.robots else "none"
        return result
