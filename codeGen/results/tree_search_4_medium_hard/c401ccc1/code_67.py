import sys

def solve():
    q = int(sys.stdin.readline())
    dp = [[False] * (1 << 30) for _ in range(1 << 30)]

    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        while u & v:
            v &= u
        dp[u][v] = True

        print("YES" if dp[v][u] else "NO")

solve()
