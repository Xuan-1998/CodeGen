def is_palindrome(s):
    return s == s[::-1]

n = int(input())
s = input()

min_cuts = 0

for i in range(n):
    if not is_palindrome(s[i:n+1]):
        min_cuts += 1

print(min_cuts)
