import sys

def min_operations(arr):
    n = len(arr)
    operations = 0
    
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            # Calculate the difference between the two elements
            diff = arr[i] - arr[i+1]
            
            # Add the difference to the total operations count
            operations += diff + 1
    
    return operations

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
print(min_operations(arr))
