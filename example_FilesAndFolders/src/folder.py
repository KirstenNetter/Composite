from .node import FileSystemNode

# Composite: Ordner
class Folder(FileSystemNode):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def display(self, indent=0):
        print(' ' * indent + f"Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)

    def count_items(self):
        total_count = 1
        for child in self.children:
            total_count += child.count_items()
        return total_count

    def calculate_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.calculate_size()
        return total_size