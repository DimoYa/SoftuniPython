symbols = ["-", ",", ".", "!", "?"]
replacement = "@"

with open("text.txt", "r") as file:
    text = file.readlines()

    for i in range(len(text)):
        if i % 2 == 0:
            even_line = text[i]
            for sym in symbols:
                if sym in even_line:
                    even_line = even_line.replace(sym, replacement)
            print(" ".join(list(reversed(even_line.split()))))