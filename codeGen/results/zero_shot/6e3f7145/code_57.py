s = input()
n = len(s)
palindromes = []
for i in range(n):
    for j in range(i+1, n+1):
        substring = s[i:j]
        if substring == substring[::-1]:
            palindromes.append(substring)
max_palindrome = max(palindromes, key=len)
print(max_palindrome)
