import sys

def solve():
    n = int(sys.stdin.readline())
    appearance_times = list(map(int, sys.stdin.readline().split()))
    healths = list(map(int, sys.stdin.readline().split()))

    # Sort the monsters by their appearance times
    sorted_monsters = sorted(zip(appearance_times, healths), key=lambda x: x[0])

    min_mana = 0

    for _, health in sorted_monsters:
        while min_mana < health:
            min_mana += 1

    print(min_mana)

if __name__ == "__main__":
    solve()
