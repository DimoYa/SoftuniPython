class Player:
    _used_names = set()

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name not valid!")
        if value in Player._used_names:
            raise Exception(f"Name {value} is already used!")
        if hasattr(self, '_name'):
            Player._used_names.discard(self._name)
        self._name = value
        Player._used_names.add(value)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self._age = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Stamina not valid!")
        self._stamina = round(value, 1)

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
