import sys

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    dp = [[0] * 100001 for _ in range(n+1)]
    max_length = 0
    
    for i in range(1, n+1):
        for j in range(max_length+1):
            if j < len(strings[i-1]):
                if strings[i-1][j] >= strings[i-2][max_length]:
                    dp[i][j] = costs[i-1] + dp[i-1][max_length]
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
        
        max_length = max(max_length, len(strings[i-1]))
    
    return min(dp[n])

print(solve())
