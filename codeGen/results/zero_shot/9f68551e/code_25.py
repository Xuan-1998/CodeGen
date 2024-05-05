import sys

def min_mana_required(n, k, h):
    k.sort()  # Sort monsters by appearance time
    mana = 0  # Initialize minimum mana required
    for i in range(n):
        while k[i] > h[i]:
            mana += 1  # Need to cast a spell with damage 1 (or x+1)
            k[i] -= 1  # Decrement monster's appearance time by 1 second
        mana += max(h[i] - k[i], 0)  # Calculate minimum mana required for this monster
    return mana

# Read input from stdin
n = int(sys.stdin.readline())
k = [int(x) for x in sys.stdin.readline().split()]
h = [int(x) for x in sys.stdin.readline().split()]

# Calculate and print the result
print(min_mana_required(n, k, h))
