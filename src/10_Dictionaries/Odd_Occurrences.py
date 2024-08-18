words = [word for word in input().split()]

words_dict = {}

for word in words:
    word = word.lower()
    if word not in words_dict:
        words_dict[word] = 0
    words_dict[word] += 1

for word in words_dict:
    if words_dict[word] % 2 != 0:
        print(word, end=" ")

