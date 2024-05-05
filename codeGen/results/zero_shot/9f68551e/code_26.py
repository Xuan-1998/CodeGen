import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        k = list(map(int, sys.stdin.readline().split()))
        h = list(map(int, sys.stdin.readline().split()))
        mana_used = 0
        for i in range(n):
            mana_used += max(k[i] - (i + 1), 0)
        print(mana_used)

solve()
