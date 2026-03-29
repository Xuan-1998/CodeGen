import sys

def can_cross_river(stones):
    # Read input
    stones = [int(x) for x in sys.stdin.read().split()]

    # Check if first jump is possible
    if stones[1] - stones[0] not in [i-1 for i in range(2, min(sstones[1]-stones[0], 3))]:
        return False

    # Check each subsequent jump
    for i in range(1, len(stones)-1):
        if abs(stones[i+1] - stones[i]) not in [i-1 for i in range(2, min(abs(stones[i+1]-stones[i]), 3))]:
            return False

    # Return True if all jumps are possible
    return True

# Get input from stdin and print answer to stdout
print(can_cross_river([int(x) for x in sys.stdin.read().split()]))
