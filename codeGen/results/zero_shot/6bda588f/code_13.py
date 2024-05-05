import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        f = sum(x * (n - i) // 2 for i, x in enumerate(a))
        print(f)

solve()
