from src.file import File
from src.folder import Folder

if __name__ == "__main__":
    # Wurzelverzeichnis
    root = Folder("root")

    # Dateien und Ordner
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    subfolder1 = Folder("subfolder1")
    subfolder1.add(File("file3.txt"))
    subfolder1.add(File("file4.txt"))

    subfolder2 = Folder("subfolder2")
    subfolder2.add(File("file5.txt"))

    # Aufbau der Hierarchie
    root.add(file1)
    root.add(file2)
    root.add(subfolder1)
    root.add(subfolder2)

    # Anzeige
    root.display()
