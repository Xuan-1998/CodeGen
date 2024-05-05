import sys

q = int(input())
dp = [False] * (2**30)

for _ in range(q):
    u, v = map(int, input().split())
    while v:
        if not dp[v]:
            break
        v &= (v - 1)
    print("YES" if dp[u] else "NO")
