import sys

def min_mana(k, h):
    dp = [float('inf')] * (k + 1)
    dp[0] = 0
    
    for i in range(1, k + 1):
        if i < len(h):
            monster_health = h[i - 1]
        else:
            monster_health = float('inf')
        
        dp[i] = min(dp[max(0, i - 1)] + max(monster_health - h[j] for j in range(i) if k[j] <= i), 
                    dp[i - 1] + (i if i > 1 else 0))
    
    return dp[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    
    print(min_mana(max(k), h))
