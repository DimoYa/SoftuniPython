from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = next((w for w in self.workers if w.name == worker_name), None)

        if worker is None:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salaries = sum([w.salary for w in self.workers])
        if self.__budget < workers_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_care_money = sum([a.money_for_care for a in self.animals])
        if self.__budget < animals_care_money:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_care_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = ""
        result += f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join(repr(lion) for lion in lions) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join(repr(tiger) for tiger in tigers) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(repr(cheetah) for cheetah in cheetahs)

        return result

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if
                w.__class__.__name__ == "Vet"]  # Corrected to "Vet" if the class name is singular

        result = ""
        result += f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join(repr(keeper) for keeper in keepers) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join(repr(caretaker) for caretaker in caretakers) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join(repr(vet) for vet in vets)

        return result
