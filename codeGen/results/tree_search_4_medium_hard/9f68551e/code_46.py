import sys
from collections import defaultdict

def min_mana_required(k, h):
    n = len(k)
    dp = [(0, [i for i in range(n)])]  # base case: no more monsters to kill
    min_mana = float('inf')
    
    for second in range(max(k), 0, -1):  # iterate through each second in reverse order
        remaining_monsters = []
        for i, (monster_time, monster_health) in enumerate(zip(k, h)):
            if monster_time >= second:
                remaining_monsters.append((monster_time, monster_health))
        
        if not remaining_monsters:  # no more monsters to kill at this second
            dp.append((0, []))  # update the dynamic programming table
        else:
            min_mana_at_second = float('inf')
            for i, (monster_time, monster_health) in enumerate(remaining_monsters):
                if monster_health <= max(m[1] for m in remaining_monsters[:i]):
                    continue  # skip monsters that can be killed by previous monsters
                min_mana_at_second = min(min_mana_at_second, dp[i][0] + monster_health)
            dp.append((min_mana_at_second, []))  # update the dynamic programming table
    
    for i, (mana, _) in enumerate(dp):
        if mana < min_mana:
            min_mana = mana
            break
    
    return min_mana

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        k = list(map(int, input().split()))
        h = list(map(int, input().split()))
        
        print(min_mana_required(k, h))

if __name__ == "__main__":
    main()
