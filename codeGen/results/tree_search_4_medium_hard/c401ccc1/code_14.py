import sys

q = int(sys.stdin.readline())

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    dp = [[0] * (1 << 30) for _ in range(1 << 30)]

    for i in range(1 << 30):
        if i & 1:
            dp[i][i] = 1

    for i in range(1 << 30):
        for j in range(i):
            if (i & j) == i and dp[j][0]:
                for k in range(1 << 30):
                    dp[i][k] |= (j & k)

    print("YES" if dp[u][v] else "NO")
