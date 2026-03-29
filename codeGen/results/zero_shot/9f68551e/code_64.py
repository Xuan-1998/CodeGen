import sys

def solve():
    n = int(sys.stdin.readline().strip())
    times = list(map(int, sys.stdin.readline().split()))
    healths = list(map(int, sys.stdin.readline().split()))

    # Initialize minimum mana required
    min_mana = 0

    for time, health in zip(times, healths):
        # Calculate the minimum mana required to kill this monster
        # We'll use a simple greedy approach: cast spells at the earliest possible time that kills the monster
        while time > min_mana + 1:
            min_mana += 1
        if min_mana < health:
            min_mana = health

    print(min_mana)

if __name__ == "__main__":
    solve()
