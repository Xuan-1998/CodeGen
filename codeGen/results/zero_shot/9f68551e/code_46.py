import sys

n = int(sys.stdin.readline())
monster_info = []
for _ in range(n):
    k, h = map(int, sys.stdin.readline().split())
    monster_info.append((k, h))

monster_info.sort(key=lambda x: x[0])

total_mana = 0
prev_damage = 1

for k, h in monster_info:
    if k > 1:  # If this is not the first monster
        prev_damage = max(prev_damage + 1, h)  # Update prev_damage
    else:  # If this is the first monster
        prev_damage = h  # Set prev_damage to the health of the first monster
    total_mana += prev_damage  # Add the damage required to kill this monster to total_mana

print(total_mana)
