import sys

def can_reach_end(arr):
    max_reachable_index = 0
    for i, jump_length in enumerate(arr):
        if i <= max_reachable_index + jump_length:
            max_reachable_index = i
        else:
            return False
    return True

arr = list(map(int, sys.stdin.readline().split()))
print(can_reach_end(arr))
