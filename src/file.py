from .node import FileSystemNode

# Leaf: Datei
class File(FileSystemNode):
    def display(self, indent=0):
        print(' ' * indent + f"File: {self.name}")
