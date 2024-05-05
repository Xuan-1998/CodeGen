def can_reach(arr):
    last_index = len(arr) - 1
    current_index = 0
    max_jump = arr[0]
    
    while current_index <= last_index:
        if current_index + max_jump >= last_index:
            return True
        current_index += 1
        max_jump = min(max_jump, arr[current_index])
    
    return False

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(can_reach(arr))
