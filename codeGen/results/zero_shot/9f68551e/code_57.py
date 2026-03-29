def solve():
    n = int(input())
    monsters = []
    
    # Read in monster data and store it in a list of tuples
    for _ in range(n):
        k, h = map(int, input().split())
        monsters.append((k, h))
        
    monsters.sort()  # Sort by appearance time
    
    total_damage = 0
    total_mana = 0
    
    for monster in monsters:
        k, h = monster
        min_damage = max(h - (k - 1), 1)  # Calculate minimum damage required
        total_damage += min_damage
        total_mana += min_damage
        
    print(total_mana)

solve()
