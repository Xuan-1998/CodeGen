import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

max_or = 0
for i in range(n):
    for j in range(i + 1, n):
        substring1 = s[i:j+1]
        or_value = 0
        for c in substring1:
            or_value |= int(c)
        max_or = max(max_or, or_value)

print(bin(max_or)[2:])
