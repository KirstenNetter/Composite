from src.file import File
from src.folder import Folder

if __name__ == "__main__":
   
    root = Folder("root")

    file1 = File("file1.txt", 10)  # 10 KB
    file2 = File("file2.txt", 20)   
    file3 = File("file3.txt", 5)
    file4 = File("file4.txt", 15)
    file5 = File("file5.txt", 50)
    subfolder1 = Folder("subfolder1")
    subfolder2 = Folder("subfolder2")

    # Aufbau der Hierarchie
    root.add(file1)
    root.add(file2)
    root.add(subfolder1)
    root.add(subfolder2)

    subfolder1.add(file3)   
    subfolder1.add(file4) 
  
    subfolder2.add(file5)  

    root.display()

    print("\nTotal items in root:", root.count_items())
    print("Total size of files in root:", root.calculate_size(), "KB")
    print("Total size of files in subfolder1:", subfolder1.calculate_size(), "KB")
    print("Total size of files in subfolder2:", subfolder2.calculate_size(), "KB")
