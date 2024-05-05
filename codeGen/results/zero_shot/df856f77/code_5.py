import sys

def min_operations(arr):
    n = len(arr)
    operations = 0
    for i in range(1, n):
        if arr[i] <= arr[i-1]:
            diff = arr[i-1] - arr[i] + 1
            arr[i] += diff
            operations += diff
    return operations

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(min_operations(arr))
