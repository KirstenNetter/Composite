from .node import FileSystemNode

# Leaf: Datei
class File(FileSystemNode):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size  

    def display(self, indent=0):
        print(' ' * indent + f"File: {self.name} ({self.size} KB)")

    def count_items(self):
        return 1

    def calculate_size(self):
        return self.size
