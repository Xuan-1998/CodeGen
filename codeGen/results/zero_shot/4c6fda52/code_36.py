import sys

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(1, min(i + 1, k) + 1):
            if s[i - j + 1:i + 1] == s[:j]:
                dp[i][j] = dp[i - j][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + 1

    return dp[n - 1][k]

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    s = input()
    print(min_changes(s, k))
