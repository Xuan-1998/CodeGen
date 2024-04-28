def find_paths(arr):
    N = len(arr)
    K = int(input())
    
    dp = [[0] * (N) for _ in range(N)]
    
    dp[0][0] = 1 if arr[0][0] == K else 0
    
    for i in range(1, N):
        for j in range(N):
            if i < N-1:
                dp[i][j] += dp[i-1][j]
            if j < N-1:
                dp[i][j] += dp[i][j-1]
            
            if arr[i][j] == K:
                dp[i][j] = 1
            elif arr[i][j] > K:
                dp[i][j] = 0
    
    return sum([sum(row) for row in dp])

print(find_paths([[0]*5] for _ in range(5)))
