import sys

def can_reach_last_index(arr):
    last_index = len(arr) - 1
    current_index = 0
    
    while current_index <= last_index:
        if current_index + arr[current_index] >= last_index:
            return True
        current_index += 1
    
    return False

# Read the array from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Print the answer to stdout
print(can_reach_last_index(arr))
