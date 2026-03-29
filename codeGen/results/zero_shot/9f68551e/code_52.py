import sys

def min_mana_required(monsters):
    # Sort monsters by appearance time
    monsters.sort(key=lambda x: x[0])

    # Initialize minimum damage and mana required
    min_damage = 1
    mana_required = 0

    for monster in monsters:
        k, h = monster
        while min_damage < h:
            min_damage += 1
        mana_required += min_damage
        min_damage -= 1

    return mana_required

# Read input from stdin
n = int(sys.stdin.readline())
monsters = []
for i in range(n):
    k, h = map(int, sys.stdin.readline().split())
    monsters.append((k, h))

# Calculate and print the minimum mana required
print(min_mana_required(monsters))
