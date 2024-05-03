import sys

def solve():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    dp = [[[0] * (m+1) for _ in range(m)] for _ in range(n)]
    
    # Initialize base case
    for i in range(1, n):
        dp[i][0][s[i-1]] += 1
    
    for k in range(1, m+1):
        for j in range(1, m+1):
            for i in range(k, n):
                if s[i] == j:
                    continue
                dp[i][k][j] = min(dp[i-1][k-1][j-1] + (s[i] != j), 
                                    dp[i-1][k][j], dp[i-1][k-1][j+1] + (s[i] != j+1))
    
    return dp[-1][-1][0]

print(solve())
