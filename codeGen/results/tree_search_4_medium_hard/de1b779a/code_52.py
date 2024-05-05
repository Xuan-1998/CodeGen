import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    profits = [list(map(int, input().split())) for _ in range(m)]
    
    dp = [[0, 0] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(min(i, m)+1):
            ai, bi, ci, di = profits[j-1]
            if i - ci >= 0:
                dp[i][0] = max(dp[i][0], dp[i-ci][0] + di)
            dp[i][1] = max(dp[i][1], dp[i-1][1])
    
    return max(max(row) for row in dp)

print(solve())
