import sys

def min_mana(n, k, h):
    # Sort the monsters by their appearance times (k)
    sorted_k = [int(x) for x in sys.stdin.readline().split()]
    k = sorted_k[:n]

    # Initialize minimum mana required
    min_mana_required = 0

    # Calculate minimum mana required for each monster
    for i in range(n):
        while k[i] > h[i]:
            k[i] -= 1
            min_mana_required += 1

    return min_mana_required


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    k = [int(x) for x in sys.stdin.readline().split()]
    h = [int(x) for x in sys.stdin.readline().split()]
    print(min_mana(n, k, h))
