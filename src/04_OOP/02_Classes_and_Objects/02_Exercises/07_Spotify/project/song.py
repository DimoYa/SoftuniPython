class Song:
    def __init__(self, name, length, single):
        self.single: bool = single
        self.length: float = length
        self.name: str = name

    def get_info(self):
        return f"{self.name} - {self.length}"

