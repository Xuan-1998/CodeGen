def max_score(n, k, z, arr):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: no moves
    dp[0][0] = arr[0]
    
    # Fill up the dp table row by row
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                # No move
                dp[i][j] = max(dp[i-1][j], arr[i])
            elif j <= z:
                # Leftward move
                dp[i][j] = max(dp[i-1][j-1], arr[i-1]) + arr[i]
            else:
                # Rightward move
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2] + 2*arr[i])
    
    return dp[n][k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
