n = int(input())
name_dict = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word not in name_dict:
        name_dict[word] = []

    name_dict[word].append(synonym)

for word, syn in name_dict.items():
    print(f"{word} - {', '.join(syn)}")
