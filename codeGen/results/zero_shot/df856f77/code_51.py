import sys

def min_operations(arr):
    n = len(arr)
    operations = 0
    for i in range(1, n):
        diff = arr[i] - (arr[i-1] + 1)
        if diff > 0:
            operations += diff
    return operations

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
