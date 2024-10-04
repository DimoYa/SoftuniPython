import string
result = ""

with open("text.txt", "r") as file:
    text = file.readlines()
    for i, line in enumerate(text):
        letters_count = 0
        punctoation_count = 0

        for sym in line:
            if sym in string.punctuation:
                punctoation_count += 1
            elif sym.isalpha():
                letters_count += 1

        result += f"Line {i + 1}: {line} ({letters_count})({punctoation_count})\n"

with open("output.txt", "w") as f:
    f.write(result)