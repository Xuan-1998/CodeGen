from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    signs = input()
    
    dp = [[[-float('inf')] * (n+1) for _ in range(n+1)] for _ in range(2)]
    
    for i in range(n):
        dp[0][i][0] = 0 if signs[i] == '+' else 1
        dp[1][i][0] = dp[0][i-1][0] + (1 if signs[i] == '-' else -1)
        
    for _ in range(q):
        l, r = map(int, input().split())
        
        sign_sum = sum(1 if signs[i] == '+' else -1 for i in range(l, r+1))
        
        dp[0][l-1][r-l+1] = float('inf')
        for i in range(l-1, r):
            dp[0][i][r-l+1] = min(dp[0][i][r-l+1], dp[0][i-1][r-l+1] + (1 if signs[i] == '-' else -1))
            
        print(min(dp[0][l-1][r-l+1], dp[1][l-1][r-l+1]))
        
solve()
