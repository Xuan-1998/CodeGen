import sys

def min_mana_required(monsters):
    n = len(monsters)
    monsters.sort()

    mana_required = 0
    current_damage = 1
    last_cast = 0

    for i in range(n):
        monster_appearance_time, monster_health = monsters[i]
        while monster_appearance_time > last_cast:
            mana_required += current_damage
            current_damage += 1
            last_cast += 1

        if monster_appearance_time == last_cast and current_damage >= monster_health:
            break

    return mana_required

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    monsters = []
    for i in range(n):
        appearance_time, health = map(int, sys.stdin.readline().split())
        monsters.append((appearance_time, health))
    print(min_mana_required(monsters))
