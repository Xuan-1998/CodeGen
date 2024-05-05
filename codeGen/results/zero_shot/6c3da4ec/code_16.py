import sys

n = int(input())
s = input()

max_or = 0
for i in range(n):
    for j in range(i + 1, n):
        or_val = 0
        for k in range(min(j - i, len(s) - j)):
            if s[i + k] == '1' and s[j - k - 1] == '1':
                or_val |= (1 << k)
        max_or = max(max_or, or_val)

print(bin(max_or)[2:])
