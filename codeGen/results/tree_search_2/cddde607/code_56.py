def numPaths(arr, K, N):
    dp = [[False] * (N+1) for _ in range(N+1)]
    
    # Initialize base case
    dp[N-1][N-1] = arr[0][0] == K
    
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if dp[i][j]:
                if i < N-1 and arr[i+1][j] <= K: 
                    dp[i][j+1] = True
                if j < N-1 and arr[i][j+1] <= K: 
                    dp[i+1][j] = True
    
    return 1 if dp[0][0] else 0

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPaths(arr, K, N))
