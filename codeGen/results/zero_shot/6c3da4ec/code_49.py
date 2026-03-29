import sys

n = int(input())
s = input()

max_or_value = 0

for start in range(n):
    for end in range(start + 1, n + 1):
        substring1 = s[start:end]
        substring2 = s[end:]

        or_value = int(substring1, 2) | int(substring2, 2)

        max_or_value = max(max_or_value, or_value)

print(bin(max_or_value)[2:].zfill(n))
