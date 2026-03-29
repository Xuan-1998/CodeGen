def solve():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [[False] * (n+1) for _ in range(2*n+1)]
    
    # Base case: dp[0][0] = 1
    dp[0][0] = True
    
    for i in range(1, 2*n+1):
        for j in range(min(i, n)+1):
            if p[i-1] <= p[i-j-1]:
                dp[i][j] = (dp[i-1][j-1] if j > 0 else True) or dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j] if j < n+1 else True) and dp[i-1][max(0, j-1)]
    
    return "YES" if dp[2*n][n] else "NO"

print(solve())
