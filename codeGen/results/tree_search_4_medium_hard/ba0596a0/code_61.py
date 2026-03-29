import sys

def can_cross_stones():
    n = int(input())
    stones = list(map(int, input().split()))
    
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for d in range(max(1, stones[i-1] - dp[i-2]), stones[i]):
            if d >= k:
                dp[i] = min(dp[i], dp[i-1] + 1)
    
    return dp[-1] != float('inf')

k = int(input())

print(can_cross_stones())
