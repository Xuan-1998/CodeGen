import sys

def alien_words(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i <= m:
            dp[i][i] = 2 ** i - 1
        else:
            for j in range(i - m + 1):
                if j % 2 == 0:
                    dp[i][j + m] += dp[j][m]
                else:
                    dp[i][j + m] += (dp[(i - j) // 2][m] if i > j else 0)
            dp[i][m] = min(dp[i][m], sum(dp[k][m - k] for k in range(i)))

    return dp[n][m]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_words(n, m) % (10**9 + 7))
