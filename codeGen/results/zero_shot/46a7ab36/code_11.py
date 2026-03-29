import sys

def count_words(n, m):
    mod = 10**8 + 7
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < n // 2:
                dp[i][j] = sum(dp[k][j - 1] for k in range(i + 1))
            else:
                dp[i][j] = sum(dp[k][j - 1] for k in range(n // 2 + 1))

    return sum(dp[i][m] for i in range(n + 1)) % mod

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_words(n, m))
