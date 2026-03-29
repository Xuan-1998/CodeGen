def max_score(k, z, scores):
    dp = [[0] * (z + 1) for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        for j in range(min(i, z) + 1):
            if i == 1:
                dp[i][j] = scores[0]
            else:
                right_score = dp[i-1][j] + scores[i]
                left_score = dp[max(0, i-z-1)][0] + (scores[i-z] if i > z else 0)
                dp[i][j] = max(right_score, left_score)
    
    return dp[k][0]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    print(max_score(k, z, scores))
