import sys

def count_words(n, m):
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(n):
        if i % 2 == 0:
            dp[i][0] = 1
        else:
            dp[i][0] = 1 if i == 0 else 0

    for j in range(1, m + 1):
        for i in range(n):
            if i < n - 1 and (i + 1) % 2 != 0:
                dp[i][j] += sum(dp[(i + 1) % n][:j])
            else:
                dp[i][j] = dp[-1][m - j] + (dp[i][j - 1] if i < n else 0)
    return pow(10, 8) + 7 - 1

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_words(n, m))
