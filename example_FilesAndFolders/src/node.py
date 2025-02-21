from abc import ABC, abstractmethod

class FileSystemNode(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def count_items(self):
        pass

    @abstractmethod
    def calculate_size(self):
        pass