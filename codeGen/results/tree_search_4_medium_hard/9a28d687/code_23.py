import sys

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    s = [input() for _ in range(n)]

    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, min(i, c[i-1]+1)+1):
            if i == 1:
                dp[i][j] = c[0]
            else:
                prev_cost = float('inf')
                for k in range(i):
                    if s[k] <= s[i-1]:
                        prev_cost = min(prev_cost, dp[k][j-1])
                dp[i][j] = prev_cost + c[i-1]

    return dp[n][0] if dp[n][0] < float('inf') else -1

print(solve())
