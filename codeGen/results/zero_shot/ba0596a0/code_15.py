import sys

def can_frog_cross(stones):
    k = 1
    pos = 0

    for stone in stones:
        if stone > pos + k:  # cannot jump to this stone
            return False
        pos += k
        k = min(k * 2, stone - pos)  # update maximum jump distance

    return True

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

# Print answer to stdout
print(can_frog_cross(stones))
