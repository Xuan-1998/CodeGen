code block
import sys

n = int(sys.stdin.readline())
k_monsters = list(map(int, sys.stdin.readline().split()))
k_monsters.sort()

total_mana = 0
max_damage = 0

for i in range(n):
    k = k_monsters[i]
    h = int(sys.stdin.readline())

    min_mana = (k - h) + 1
    total_mana += min_mana
    max_damage = max(max_damage, min_mana)

print(total_mana)
