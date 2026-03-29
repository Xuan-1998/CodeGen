import sys

def min_mana_required(mons_appear_time, mons_health):
    # Sort the monsters by their appearance times
    sorted_monsters = sorted(zip(mons_appear_time, mons_health))

    total_mana = 0
    prev_damage = 0

    for appear_time, health in sorted_monsters:
        # Calculate the minimum mana required to kill this monster
        min_mana_required = max(health - (appear_time - prev_damage), 1)
        total_mana += min_mana_required
        prev_damage = appear_time - min_mana_required

    return total_mana

# Read input from stdin
n_cases = int(sys.stdin.readline())
for _ in range(n_cases):
    n_monsters = int(sys.stdin.readline())
    mons_appear_time = list(map(int, sys.stdin.readline().split()))
    mons_health = list(map(int, sys.stdin.readline().split()))

    # Calculate the minimum mana required for each monster
    min_mana = min_mana_required(mons_appear_time, mons_health)

    # Print the result to stdout
    print(min_mana)
