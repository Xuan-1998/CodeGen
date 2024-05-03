def max_distance(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, n) + 1):
            if i % 2 == 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][n-j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][n-j]) - 1 if j > 0 else 1
    
    return dp[n][n//2]

if __name__ == "__main__":
    n = int(input())
    print(max_distance(n))
