import sys

def can_reach_last_index(jumps):
    max_reachable = 0
    for i in range(len(jumps)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, min(i + jumps[i], len(jumps) - 1))
    return True

# Read input from stdin
jumps = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(can_reach_last_index(jumps))
