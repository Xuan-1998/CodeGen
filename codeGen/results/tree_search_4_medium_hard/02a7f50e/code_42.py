import sys

def solve():
    n = int(input())
    dp = [[0] * 100001 for _ in range(n+1)]
    
    max_power = 0
    
    for i in range(n):
        pos, power = map(int, input().split())
        max_power = max(max_power, power)
        
        # Update dp[i][j]
        for j in range(power, -1, -1):
            if not dp[i][j]:
                dp[i+1][max(j-1, 0)] += 1
            else:
                dp[i+1][min(j, max_power)] += 1
    
    return min(dp[-1])

print(solve())
