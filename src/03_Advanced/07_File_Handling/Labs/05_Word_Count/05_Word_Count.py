import re

words = []
text = ""
result = {}

with open("words.txt") as file:
    words.extend(file.read().split())

with open("text.txt") as file:
    text += file.read()

for word in words:
    count = len(re.findall(rf'\b{re.escape(word)}\b', text, re.IGNORECASE))
    result[word] = count

sorted_result = sorted(result.items(), key=lambda x: -x[1])


with open("output.txt", "w") as f:
    for k, v in sorted(result.items(), key=lambda x: -x[1]):
        f.write(f"{k} - {v}\n")
