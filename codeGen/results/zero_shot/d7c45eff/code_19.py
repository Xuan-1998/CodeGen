import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

if k < n:
    result = s[:k]
else:
    if s[-1] <= 'z':
        result = s + s[:k-n]
    else:
        result = s[:-1]

print(result)
