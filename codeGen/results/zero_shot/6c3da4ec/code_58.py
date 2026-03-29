import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

max_or = 0
for i in range(n):
    for j in range(i+1, n):
        left = int(s[:i+1], 2)
        right = int(s[i+1:j+1], 2)
        or_value = left | right
        max_or = max(max_or, bin(or_value)[2:].zfill(len(bin(left)|bin(right))[2:]))[2:]

print(max_or)
