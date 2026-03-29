import sys

def solve(n, s):
    return sum((a - s) for a in range(1, n + 1))

t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    print(sum((a - s) for a in range(1, n + 1)))
