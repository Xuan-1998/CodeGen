def solve():
    m, N = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(N + 1)]
    
    for k in range(1, m + 1):
        dp[0][k] = 1
    
    for i in range(1, N + 1):
        for j in range(1, min(i+1, m)+1):
            for k in range(1, min(i+1, j)+1):
                dp[i][j] += dp[i-k][k]
    
    print(dp[N][m] % (10**9 + 7))

if __name__ == "__main__":
    solve()
