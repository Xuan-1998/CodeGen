def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0] * (n) for _ in range(n)]
    
    memo = {}
    
    def is_possible(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i > j:
            return 1
        
        if p[2*i]+p[2*i+1] <= p[2*j]+p[2*j+1]:
            dp[i][j] = 1
        else:
            dp[i][j] = 0
        
        memo[(i, j)] = dp[i][j]
        
        return dp[i][j]
    
    for i in range(n):
        for j in range(i, n):
            is_possible(i, j)
    
    if dp[0][n-1]:
        print("YES")
    else:
        print("NO")

solve()
