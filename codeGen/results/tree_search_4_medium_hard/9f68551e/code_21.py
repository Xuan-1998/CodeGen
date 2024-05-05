import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

dp = [[float('inf')] * (max(k) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, max(k) + 1):
        if i == n:
            dp[i][j] = 0
        else:
            last_monster_appeared_at = k[i-1] - 1
            min_mana_to_kill_monsters = float('inf')
            
            if j >= last_monster_appeared_at:
                min_mana_to_kill_monsters = min(min_mana_to_kill_monsters, dp[i-1][last_monster_appeared_at] + h[i-1])
            
            dp[i][j] = min(dp[i][min(j, k[i-1] - 1)], min_mana_to_kill_monsters)
    
print(min(dp[n]))
