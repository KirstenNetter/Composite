from abc import ABC, abstractmethod

class Stelle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def nenne_anzahl(self):
        pass
