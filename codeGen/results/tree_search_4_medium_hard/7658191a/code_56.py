def max_score(n, k, z, scores):
    dp = [[0]*(k+1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if j > 0:
                dp[i][j] = max(dp[i-1][j-1] + scores[i], dp[i-1][j])
            elif j < z+1 and i+k >= j:
                dp[i][j] = max(dp[i-1][j+1] - scores[i-1], dp[i-1][j])

    return dp[-1][-1]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    print(max_score(n, k, z, scores))
