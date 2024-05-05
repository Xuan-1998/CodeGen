import sys

def min_operations(arr):
    arr.sort()
    operations = 0
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i+1]:
            operations += (arr[i] - arr[i+1]) + 1
            arr[i+1] = arr[i]
    return operations

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
print(min_operations(arr))
