def find_ways(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(min(i, n)):
            if j == 0:
                dp[i][j] = 1
            elif j == 1:
                dp[i][j] = i
            else:
                for k in range(j + 1):
                    dp[i][j] += dp[k][0] * (dp[i - k - 1][j - k] - dp[i - k - 1][j - k])
    
    return dp[n][n] % (10**9 + 7)

if __name__ == "__main__":
    n = int(input())
    print(find_ways(n))
