import sys

def can_frog_cross(stones):
    prev_jump = 0
    for i, pos in enumerate(stones):
        if i == 0 or pos - stones[i-1] > abs(pos - prev_jump) + 2:
            return False
        prev_jump = pos - stones[i-1]
    return True

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(can_frog_cross(stones))
