import sys

def can_reach_last_index(jumps):
    max_reachable = 0
    for i in range(len(jumps)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + jumps[i])
    return True

# Example usage:
jumps = [2, 3, 1, 1, 4]
if can_reach_last_index(jumps):
    print("It's possible to reach the last index.")
else:
    print("It's not possible to reach the last index.")

