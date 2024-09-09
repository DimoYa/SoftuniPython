import re

line = input()
pattern = r"([@#])(?P<word1>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1"
matches = re.finditer(pattern, line)
mirror_words = {}

words = [math.groupdict() for math in matches]

for word in words:
    word1 = word['word1']
    word2 = word['word2']

    if word1 == word2[::-1]:
        mirror_words[word1] = word2

if words:
    print(f"{len(words)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(", ".join([f"{w1} <=> {w2}" for w1, w2 in mirror_words.items()]), end="")
else:
    print("No mirror words!", end="")
