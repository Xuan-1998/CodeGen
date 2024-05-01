def findPaths(arr):
    n = len(arr)
    k = int(input())
    dp = [[0] * (n) for _ in range(n)]
    
    # Fill up the first row and column, because we can only move down or right
    for i in range(1, n):
        if arr[0][i-1] <= k:
            dp[i][0] = 1
        else:
            break
    
    for j in range(1, n):
        if arr[j-1][0] <= k:
            dp[0][j] = 1
        else:
            break
    
    # Fill up the rest of the table
    for i in range(1, n):
        for j in range(1, n):
            if arr[i][j] <= k and (dp[i-1][j] > 0 or dp[i][j-1] > 0):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif arr[i][j] <= k:
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n-1][n-1]

print(findPaths(list(map(int, input().split()))))
