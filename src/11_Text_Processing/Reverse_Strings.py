string_word = input()

while not string_word == "end":
    print(f"{string_word} = {string_word[::-1]}")
    string_word = input()
