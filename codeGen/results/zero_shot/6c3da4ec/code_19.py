import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

max_value = 0
current_max_or = 0

for i in range(n):
    for j in range(i+1, n+1):
        substring = s[i:j]
        or_value = int(substring, 2)
        current_max_or = max(current_max_or, or_value)
        max_value = max(max_value, current_max_or)
        current_max_or = 0

print(bin(max_value)[2:])
