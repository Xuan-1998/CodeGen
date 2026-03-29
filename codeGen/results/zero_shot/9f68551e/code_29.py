import sys

def solve_monster_monsters(monsters):
    # Sort monsters by appearance time
    monsters.sort(key=lambda x: x[1])
    
    total_mana = 0
    prev_damage = 0
    
    for monster in monsters:
        health, k_i = monster
        while k_i > 0:
            if prev_damage >= health:
                break
            total_mana += prev_damage + 1
            prev_damage += 1
            k_i -= 1
        else:
            total_mana += health
    
    return total_mana

t = int(input())
for _ in range(t):
    n = int(input())
    monsters = [(int(input()), int(input())) for _ in range(n)]
    print(solve_monster_monsters(monsters))
