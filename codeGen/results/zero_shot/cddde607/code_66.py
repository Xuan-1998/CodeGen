def count_paths(arr, K, N):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[0][0]
            elif i > 0 and j == 0:
                dp[i][j][0] = dp[i-1][j][0] + arr[i][0]
            elif i == 0 and j > 0:
                dp[i][j][0] = dp[i][j-1][0] + arr[0][j]
            else:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) + arr[i][j]

    count = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j][K-1] == K:
                count += 1

    return count
