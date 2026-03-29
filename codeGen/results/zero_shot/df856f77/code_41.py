def min_operations(arr):
    n = len(arr)
    operations = 0
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            # Decrease the current element to make room for the larger value
            operations += arr[i] - arr[i+1]
        elif arr[i] < arr[i+1]:
            # Increase the current element to accommodate the larger value
            operations += arr[i+1] - arr[i]
    
    return operations

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(min_operations(arr))
