import sys

def min_operations(arr):
    n = len(arr)
    operations = 0
    
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            # need to decrease or increase arr[i]
            if arr[i] > arr[i+1]:
                # need to decrease arr[i]
                operations += arr[i] - arr[i+1]
            else:
                # need to increase arr[i]
                operations += arr[i+1] - arr[i]
    
    return operations

# Read input from stdin
n = int(input())
arr = [int(x) for x in input().split()]

# Calculate and print the minimum number of operations
print(min_operations(arr))
