import sys

def max_score(scores, k, z):
    n = len(scores)
    dp = [[0] * (z + 1) for _ in range(k + 1)]

    # Base case: when k = 0
    for j in range(z + 1):
        dp[0][j] = sum(scores[:j])

    for i in range(1, k + 1):
        for j in range(min(i, z) + 1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], dp[i-z][z]) + scores[i]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-z][z]) + scores[i]

    return dp[k][0]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    print(max_score(scores, k, z))
