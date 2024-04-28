def solve():
    k, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = 1
    
    for i in range(1, n):
        for j in range(1, n):
            for c in range(k + 1):
                if arr[i][j] <= c:
                    dp[i][j][c] = 0
                else:
                    dp[i][j][c] += sum(dp[i-1][j][c-coin] for coin in [arr[i-1][j], arr[i][j-1]])
                    
    return dp[-1][-1][k]

print(solve())
