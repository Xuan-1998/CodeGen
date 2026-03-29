import sys

def min_operations(arr):
    n = len(arr)
    operations = 0
    
    for i in range(n - 1):
        if arr[i] >= arr[i + 1]:
            # Out of order, need to move up
            diff = arr[i] - arr[i + 1]
            operations += diff
            arr[i + 1] = arr[i] + 1
    
    return operations

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(min_operations(arr))
