def alien_words(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i + 1, m + 1)):
            if j == 1:
                dp[i][j] = 1
            else:
                if 2 * (i - 1) <= n:
                    dp[i][j] += dp[max(0, i - 2)][j - 1]
                if 2 * i > n or j == m:
                    dp[i][j] += dp[i - 1][j - 1]

    return pow(10, 8 + 7, dp[n][m])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_words(n, m))
