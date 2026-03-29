def max_score(n, k, z, scores):
    dp = [[[0] * (z + 1) for _ in range(k + 1)] for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if j <= i:
                left_score = dp[i - 1][j - 1][z] + scores[i]
            else:
                left_score = 0

            right_score = dp[i - 1][j][z] + scores[i]

            if j > 0 and z > 0:
                max_score = max(left_score, right_score)
            elif j == 0 or z == 0:
                max_score = scores[i]
            else:
                max_score = max(left_score, right_score)

            dp[i][j][z] = max_score

    return dp[n - 1][k][z]

# Read input
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    scores = list(map(int, input().split()))
    
    # Calculate the maximum score
    max_score = max_score(n, k, z, scores)

    print(max_score)
