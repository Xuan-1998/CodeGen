import sys

def max_score(scores, k, z):
    n = len(scores)
    dp = [[0] * (z + 1) for _ in range(k + 1)]

    # Base case: when k is 0, the maximum score is simply the sum of all values in the array
    for i in range(1, n + 1):
        dp[0][i - 1] = scores[i]

    # Fill up the table
    for i in range(1, k + 1):
        for j in range(min(i, z) + 1):
            if i == 1:
                dp[i][j] = max(dp[i-1][j], scores[1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + scores[i])

    return dp[k][z]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    print(max_score(scores, k, z))
