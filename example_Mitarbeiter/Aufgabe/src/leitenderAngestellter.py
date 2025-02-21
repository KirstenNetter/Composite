from .stelle import Stelle

# Composite: Ordner
class LeitenderAngestellter(Stelle):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def display(self, indent=0):
        print(' ' * indent + f"Leitender Angestellter: {self.name}")
        for child in self.children:
            child.display(indent + 2)

    def nenne_anzahl(self):       
        pass
        
  