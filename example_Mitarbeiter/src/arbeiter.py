from .stelle import Stelle

# Leaf: Employee
class Arbeiter(Stelle):
    def __init__(self, name):
        super().__init__(name)

    def display(self, indent=0):
        print(' ' * indent + f"Arbeiter: {self.name} ")

    def nenne_anzahl(self):
        pass
        