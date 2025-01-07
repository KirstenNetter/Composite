from src.file import File
from src.folder import Folder

if __name__ == "__main__":
   
    root = Folder("root")

    file1 = File("file1.txt", 10)  # 10 KB
    file2 = File("file2.txt", 20)  # 20 KB
    subfolder1 = Folder("subfolder1")
    subfolder1.add(File("file3.txt", 5))   # 5 KB
    subfolder1.add(File("file4.txt", 15))  # 15 KB

    subfolder2 = Folder("subfolder2")
    subfolder2.add(File("file5.txt", 50))  # 50 KB

    # Aufbau der Hierarchie
    root.add(file1)
    root.add(file2)
    root.add(subfolder1)
    root.add(subfolder2)

    root.display()

    print("\nTotal items in root:", root.count_items())

    print("Total size of files in root:", root.calculate_size(), "KB")
