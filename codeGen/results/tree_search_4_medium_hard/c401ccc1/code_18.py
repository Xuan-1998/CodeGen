import sys

q = int(sys.stdin.readline())
dp = [[False] * (1 << 30) for _ in range(1 << 30)]

for _ in range(int(sys.stdin.readline())):
    u, v = map(lambda x: int(x), sys.stdin.readline().split())

    while u & v != v:
        v &= u

    for i in range((1 << 30) - 1, -1, -1):
        if dp[u][i]:
            j = i
            while j & v != v:
                j &= i
            dp[v][j] = True

for _ in range(q):
    u, v = map(lambda x: int(x), sys.stdin.readline().split())
    print("YES" if dp[u][v] else "NO")
