def count_paths(arr):
    N = len(arr)
    K = int(input())
    
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    
    for i in range(1, N):
        dp[i][0] = 0 if arr[i-1][0] > K else dp[i-1][0]
    for j in range(1, N):
        dp[0][j] = 0 if arr[0][j-1] > K else dp[0][j-1]
    
    for i in range(1, N):
        for j in range(1, N):
            if arr[i][j] <= K:
                if arr[i-1][j] <= K and arr[j-1][i] <= K:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1]

print(count_paths([[int(x) for x in input().split()] for _ in range(int(input()))]))
