from abc import ABC, abstractmethod

# Component: Basisklasse für Dateien und Ordner
class FileSystemNode(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass
