import sys

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Calculate the minimum number of operations
ops = 0
while len(str(x)) < n:
    ops += 1
    x *= 10

if len(str(x)) == n:
    print(ops)
else:
    print(-1)
