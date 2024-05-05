import sys

def min_operations():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    operations = 0
    
    for i in range(n - 1):
        if arr[i] >= arr[i + 1]:
            diff = arr[i] - arr[i + 1]
            arr[i + 1] += diff
            operations += diff
    
    return operations

print(min_operations())
