import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

max_or = 0
for i in range(n):
    for j in range(i+1, n):
        substr1 = s[i:j+1]
        or_val = int(substr1, 2)
        max_or = max(max_or, or_val)

print(format(max_or, 'b').lstrip('0'))
