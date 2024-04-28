def numPathsWithKCoins(arr, K, N):
    dp = [[0] * (N) for _ in range(N)]
    
    # Base case: There's only one way to collect all coins at the bottom right corner.
    dp[N-1][N-1] = 1
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= K:
                # If there are enough coins, consider moving down and right.
                if i < N - 1:
                    dp[i+1][j] += dp[i][j]
                if j < N - 1:
                    dp[i][j+1] += dp[i][j]
    
    return dp[0][0]

# Test the function
K = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(numPathsWithKCoins(arr, K, N))
