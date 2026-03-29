def solve():
    n = int(input())
    monsters = []
    for _ in range(n):
        k, h = map(int, input().split())
        monsters.append((k, h))
    
    monsters.sort()
    mana = 0
    prev_damage = 1
    
    for monster in monsters:
        while True:
            if mana + prev_damage >= monster[1]:
                break
            mana += 1
            prev_damage += 1
    
    print(mana)

solve()
