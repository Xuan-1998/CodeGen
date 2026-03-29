def max_score(n, k, z, array):
    dp = [[[0] * (z + 1) for _ in range(k + 1)] for _ in range(n)]
    for i in range(1, n + 1):
        dp[i][0][0] = array[i - 1]
    
    for i in range(1, n + 1):
        for j in range(z + 1):
            if j > 0:
                if i < n:
                    dp[i][j][1] = max(dp[i - 2][j - 1][1], dp[i - 1][j][1])
                else:
                    dp[i][j][1] = max(dp[i - 1][j][1], 0)
            if j < z:
                if i > 1:
                    dp[i][j][2] = max(dp[i + 1][j][2], dp[i - 1][j][2])
                else:
                    dp[i][j][2] = max(dp[i][j][2], 0)
            for l in range(3):
                if l == 0 and i < n:
                    dp[i][j + l][l] = max(dp[i - 1][j][l], array[i])
                elif l == 1 and i > 1:
                    dp[i][j + l][l] = max(dp[i - 2][j - 1][l], array[i - 1])
                else:
                    dp[i][j + l][l] = max(dp[i][j][l], array[i])
    return max(dp[1][k][0], dp[1][k][1], dp[1][k][2])

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    array = list(map(int, input().split()))
    print(max_score(n, k, z, array))
