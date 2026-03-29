import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        k = list(map(int, sys.stdin.readline().split()))
        h = list(map(int, sys.stdin.readline().split()))

        # Sort monsters by appearance time
        sorted_k = sorted(zip(k, h), key=lambda x: x[0])

        # Initialize maximum damage and mana used so far
        max_damage = 1
        mana_used = 0

        for _, health in sorted_k:
            # Find the minimum damage needed to kill this monster
            while max_damage < health:
                max_damage += 1

            # Update mana used and reset maximum damage
            mana_used += max_damage
            max_damage = 1

        print(mana_used)

if __name__ == "__main__":
    solve()
