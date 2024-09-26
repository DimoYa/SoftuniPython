def palindrome(word, index):
    if len(word) // 2 == index:
        return f"{word} is a palindrome"
    if word[index] == word[-(index + 1)]:
        return palindrome(word, index + 1)
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))


