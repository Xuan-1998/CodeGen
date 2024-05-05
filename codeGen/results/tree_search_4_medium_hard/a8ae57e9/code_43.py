import sys

def solve():
    n = int(input())
    k = int(input())
    dp = [[0] * (1001) for _ in range(k+1)]
    
    for i in range(n):
        size, spend = map(int, input().split())
        
        for j in range(min(k, size), -1, -1):
            for t in range(j-1, -1, -1):
                dp[t][j] = max(dp[t][j], dp[t-1][max(0, j-size)] + spend)
    
    return dp[k][n],

# Read the input and print the output
_, output = solve()
print(*output)
