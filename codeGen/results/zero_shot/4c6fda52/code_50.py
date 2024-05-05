import sys

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if s[i - 1] != 'RGB'[j % 3]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][k]

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    print(min_changes(input().strip(), k))
