import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        length = 0
        while m > 0:
            m -= 1
            n = sum(int(d) + 1 for d in str(n))
            length += 1
        print(length % (10**9 + 7))

solve()
