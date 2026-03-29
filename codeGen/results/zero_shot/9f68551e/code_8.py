import sys

def solve():
    n = int(sys.stdin.readline())
    monsters = []
    for _ in range(n):
        k, h = map(int, sys.stdin.readline().split())
        monsters.append((k, h, 0))
    
    monsters.sort()
    
    total_mana = 0
    
    for i, (k, h, _) in enumerate(monsters):
        if i == 0:
            damage = 1
        else:
            min_damage = max(monster[2] for monster in monsters[:i]) + 1
            if min_damage > h:
                min_damage = h
            damage = min_damage - 1
        
        total_mana += damage
        h -= damage
    
    print(total_mana)

if __name__ == "__main__":
    solve()
