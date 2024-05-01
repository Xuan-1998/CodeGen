from sys import stdin

def count_paths(arr, K):
    N = len(arr)
    dp = [[0 for _ in range(K+1)] for _ in range(N)]
    
    # Initialize the first row and column
    for i in range(N):
        dp[i][0] = 1
    
    for i in range(1, N):
        for j in range(1, min(i+1, K)+1):
            if arr[i-1][j-1] <= K:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
    
    return dp[N-1][K]

# Read input from stdin
K, N = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

print(count_paths(arr, K))
