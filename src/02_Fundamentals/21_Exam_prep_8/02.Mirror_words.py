import re

line = input()
pattern = r"([@#])(?P<word_1>[A-Za-z]{3,})\1\1(?P<word_2>[A-Za-z]{3,})\1"
matches = re.finditer(pattern, line)
pairs = 0
pairs_dict = {}

for match in matches:
    word_1 = match.group("word_1")
    word_2 = match.group("word_2")
    pairs += 1

    if word_1 == word_2[::-1]:
        pairs_dict[word_1] = word_2

if not pairs:
    print("No word pairs found!")
else:
    print(f"{pairs} word pairs found!")

if not len(pairs_dict):
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join([f"{w1} <=> {w2}" for w1, w2 in pairs_dict.items()]))