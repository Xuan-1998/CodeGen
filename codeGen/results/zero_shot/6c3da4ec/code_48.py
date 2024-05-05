import sys
n = int(input())
s = input()
max_or = 0

for i in range(n):
    for j in range(i+1, n):
        left = int(s[:i], 2)
        right = int(s[i:j], 2)
        or_val = left | right
        max_or = max(max_or, or_val)

print(bin(max_or)[2:])
