def solve():
    n = int(input())
    M = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][i] = 1
        for j in range(i - 1, -1, -1):
            dp[i][j] = sum(dp[k][j] * (M[k] <= M[j]) for k in range(j, i)) % (10**9 + 7)
    
    return str(dp[n][0])

print(solve())
