from itertools import product

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[[float('inf')] * (max(a) + 1) for _ in range(max(2*s, max(a)))] for _ in range(n+1)]
    x = [[0] * (max(a)+1) for _ in range(n+1)]
    y = [[0] * (max(a)+1) for _ in range(n+1)]

    dp[1][a[0]][a[0]] = 0

    for i in range(2, n+1):
        for j in range(max(-a[i-1], 0), min(a[i-1], s)):
            for k in range(min(a[i-1], s), max(a[i-1], s)):
                if (k - j) * (a[i-1] - k) >= 0:
                    dp[i][j][k] = min(dp[i-1][l][m] + (a[i-1] - m) * (s-j) for l, m in product(range(k+1), range(a[i-1]-k)))
        x[i][0] = a[i-1]
        y[i][0] = 0

    print(dp[n][s][a[n]])
