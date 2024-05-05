import sys

def min_mana_required():
    n = int(sys.stdin.readline())
    monsters = []
    
    for _ in range(n):
        k_i, h_i = map(int, sys.stdin.readline().split())
        monsters.append((k_i, h_i))
    
    monsters.sort(key=lambda x: x[0])
    
    mana_spent = 0
    min_mana = 0
    
    for monster in monsters:
        while mana_spent < monster[0]:
            mana_spent += 1
        
        if mana_spent >= monster[1]:
            min_mana = max(min_mana, mana_spent - (monster[0] - 1))
    
    print(mana_spent)
