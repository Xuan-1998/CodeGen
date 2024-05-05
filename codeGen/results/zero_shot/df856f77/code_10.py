import sys

def min_operations(arr):
    operations = 0
    nxt = arr[0]
    
    for num in arr[1:]:
        if num <= nxt:
            operations += nxt - num + 1
            nxt = num
        else:
            nxt = num
    
    return operations

# Read input from stdin
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Calculate and print the minimum number of operations
print(min_operations(arr))
