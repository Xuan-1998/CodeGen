import sys

def max_score(n, k, z, arr):
    memo = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        memo[i][0] = 0
    for j in range(k + 1):
        memo[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j <= z:
                max_left = memo[i - 1][j - 1]
                left_score = arr[i - 1] + (i > 1 and memo[i - 2][j - 1] or 0)
                right_score = arr[i] + (memo[i - 1][j - 1] or 0)
                dp[i][j] = max(max_left, left_score, right_score)
            else:
                max_left = memo[i - 1][j - 1]
                left_score = arr[i - 1] + (i > 1 and memo[i - 2][j - 1] or 0)
                dp[i][j] = max(max_left, left_score)
            memo[i][j] = dp[i][j]

    return memo[n][k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
