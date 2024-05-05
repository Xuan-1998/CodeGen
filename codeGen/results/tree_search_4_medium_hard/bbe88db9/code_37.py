def portal_moves():
    n = int(input())
    p = list(map(int, input().split()))
    
    memo = [[[0] * (n+1) for _ in range(2)] for _ in range(n+1)]
    
    def dp(i, j, k):
        if k < 0:
            return float('inf')
        if k == 0:
            return 0
        if memo[i][j][k] != 0:
            return memo[i][j][k]
        
        if j % 2 == 1: # odd number of crosses, use the second portal
            dp_val = 1 + dp(p[i-1], (p[i-1]-1)//2, k-1)
        else: # even number of crosses, use the first portal
            dp_val = 1 + dp(i-1, j-1, k-1)
        
        memo[i][j][k] = dp_val
        
        return dp_val
    
    return dp(0, n+1, n) % (10**9 + 7)

print(portal_moves())
