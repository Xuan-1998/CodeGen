import sys

def min_f(a, s):
    n = len(a)
    f = sum(x * y for x, y in zip(map(lambda x: x // 2, a), map(lambda x: x - x // 2, a))) + sum(min(x, s) * (a[i] - min(x, s)) for i, x in enumerate(a))
    return f

t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(min_f(a, s))
