import sys

def min_mana_required(appearance_times, healths):
    # Sort the monsters by their appearance time
    sorted_monsters = sorted(zip(appearance_times, healths))

    # Initialize the minimum mana required
    min_mana = 0

    for monster in sorted_monsters:
        # Calculate the minimum mana required to kill this monster
        while True:
            if min_mana >= monster[1]:
                break
            min_mana += 1

    return min_mana

n = int(sys.stdin.readline())
appearance_times = [int(x) for x in sys.stdin.readline().split()]
healths = [int(x) for x in sys.stdin.readline().split()]

min_mana_required(appearance_times, healths)
