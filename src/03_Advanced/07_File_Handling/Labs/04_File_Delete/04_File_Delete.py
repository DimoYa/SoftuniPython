import os

try:
    os.remove("../03_File_Writer/my_first_file.txt")
    print("File Deleted")
except FileNotFoundError:
    print("File already deleted!")
