def maximum_score(n, k, z, scores):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = sum(scores[:i])

    for j in range(1, k + 1):
        for i in range(j, n + 1):
            max_score = 0
            if i > 1:
                max_score = max(max_score, dp[i - 2][j - 1] - scores[i - 1])
            if j < z or j == 0:
                max_score = max(max_score, dp[i - 1][j - 1] + scores[i])

            dp[i][j] = max_score

    return dp[n][k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    print(maximum_score(n, k, z, scores))
