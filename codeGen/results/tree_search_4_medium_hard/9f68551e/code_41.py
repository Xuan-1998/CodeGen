import sys

def min_mana_required():
    n = int(input())  # number of monsters
    
    monster_appearances = list(map(int, input().split()))  # array of monster appearances
    monster_healths = list(map(int, input().split()))  # array of monster healths
    
    dp = [0] * (monster_appearances[-1] + 1)  # DP table for minimum mana required at each time step
    
    max_health = 0  # maximum health of monsters seen so far
    for i in range(n):
        while monster_appearances[i] > 0:
            dp[monster_appearances[i]] = max(dp[monster_appearances[i]], max_health + 1)
            max_health = max(max_health, monster_healths[i])
            monster_appearances[i] -= 1
    
    return min(dp)  # minimum mana required to kill all monsters

print(min_mana_required())
