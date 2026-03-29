import sys

n = int(input())
s = input()

max_or = 0
for i in range(n):
    for j in range(i+1, n):
        or_result = 0
        for k in range(min(i+1, j), max(i+1, j)):
            or_result |= int(s[k])
        max_or = max(max_or, or_result)

print(bin(max_or)[2:].zfill(n))
