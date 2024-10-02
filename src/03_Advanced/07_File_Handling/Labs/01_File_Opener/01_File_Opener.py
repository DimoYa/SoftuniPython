try:
    with open('text.txt', 'r') as file:
        file.read()
        print("File found")
except FileNotFoundError:
    print("File not found")