import sys

def min_mana_required(n, monsters):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = monsters[0][2]
        else:
            dp[i] = min(dp[i - 1], dp[i - 1] + (monsters[i-1][1] - monsters[i-2][1]) * (monsters[i-1][2] - 1))
    
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    monsters = []
    for _ in range(n):
        k, h = map(int, input().split())
        monsters.append((k, h))
    
    print(min_mana_required(n, monsters))
