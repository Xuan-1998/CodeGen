import sys

s = input().strip()
count_a = 0
count_b = 0

for c in s:
    if c == 'A':
        count_a += 1
    elif c == 'B':
        count_b += 1

if (count_a >= count_b) and ((len(s) - count_a) % 2 == 0 or (len(s) - count_b) % 2 == 0):
    print("YES")
else:
    print("NO")
