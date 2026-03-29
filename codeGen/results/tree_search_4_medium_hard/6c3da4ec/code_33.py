import sys

n = int(input())
s = input()

dp = {}
max_or = 0
for i in range(n):
    or_value = 0
    one_count = 0
    for j in range(i, n):
        if s[j] == '1':
            one_count += 1
            or_value |= (1 << one_count)
        dp[(i, j)] = or_value
        max_or = max(max_or, or_value)

print(max_or)
