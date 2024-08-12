words = input().split()
palindrome_word = input()

palindromes = [p for p in words if p == p[::-1]]

print(palindromes)
print(f"Found palindrome {words.count(palindrome_word)} times")
