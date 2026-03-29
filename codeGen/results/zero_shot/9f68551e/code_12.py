import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        k = list(map(int, sys.stdin.readline().split()))
        h = list(map(int, sys.stdin.readline().split()))

        # Sort monsters by appearance time
        sorted_monsters = [(k_i, h_i) for (k_i, h_i) in zip(k, h)]
        sorted_monsters.sort()

        # Initialize minimum mana required
        min_mana = 0

        # Iterate through the sorted monsters and calculate minimum mana required
        for i in range(len(sorted_monsters)):
            monster_k, monster_h = sorted_monsters[i]
            while monster_h > 1:
                monster_h -= 2
                min_mana += 1
            if monster_h > 0:
                min_mana += monster_h

        print(min_mana)

solve()
