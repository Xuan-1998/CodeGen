import sys

def min_F(a, s):
    n = len(a)
    f = sum([min((a[i] - s) * (s - i), (i - s) * (a[i] - s)) for i in range(n)])
    return f


t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(min_F(a, s))
