n = int(input())
moods = list(map(int, input().split()))

dp = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(3):
    dp[i][i] = True

for i in range(1, n + 1):
    for j in range(i + 1):
        if moods[j % n] == 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = any(dp[i - 1][k] for k in range(j))

print("YES" if dp[n][n // 2] else "NO")
