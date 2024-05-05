import sys

def can_cross_stones(stones):
    n = len(stones)
    dp = {0: True}
    
    for i in range(1, n):
        dp[i] = False
        for j in range(max(0, i - 3), min(i, n-1)):
            if stones[j + 1] <= stones[i]:
                dp[i] = dp.get(j, False) or dp[i]
    
    return dp[-1]

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

print(can_cross_stones(stones))
