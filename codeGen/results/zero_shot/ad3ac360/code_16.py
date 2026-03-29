import sys

def is_palindrome(s):
    return s == s[::-1]

n = int(input())
s = input()

cuts = 0
for i in range(1, n):
    if not is_palindrome(s[:i+1]):
        cuts += 1

print(cuts)
