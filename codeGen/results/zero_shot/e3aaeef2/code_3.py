import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        print(len(str(n)) % (10**9 + 7))

solve()
