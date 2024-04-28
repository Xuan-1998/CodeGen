def count_paths(arr):
    n = len(arr)
    k = int(input())
    dp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = arr[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j][0] = dp[i-1][j][0] + arr[i][j]
            else:
                dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j-1][0] + arr[i][j]
            
            for coin in range(1, k+1):
                if j == 0:
                    dp[i][j][coin] = max(dp[i-1][j][coin-1], dp[i-1][j][coin]) + arr[i][j]
                else:
                    dp[i][j][coin] = max(dp[i-1][j-1][coin-1], dp[i-1][j][coin]) + arr[i][j]
                    
    return dp[-1][-1][-1]

print(count_paths([[int(i) for i in input().split()] for _ in range(int(input()))]))
