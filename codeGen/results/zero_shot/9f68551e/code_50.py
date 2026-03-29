import sys

def min_mana_required(k, h):
    # Sort monsters by appearance time
    monster_times = sorted(zip(k, h))

    # Initialize minimum mana required
    min_mana = 0

    # Iterate over monsters
    for i in range(len(monster_times)):
        k_i, h_i = monster_times[i]

        # Calculate the minimum damage required to kill this monster
        min_damage = max(1, h_i)

        # Update minimum mana required
        min_mana += min_damage

    return min_mana

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    k = [int(x) for x in sys.stdin.readline().split()]
    h = [int(x) for x in sys.stdin.readline().split()]

    print(min_mana_required(k, h))
