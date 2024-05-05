import sys

def min_operations(arr):
    n = len(arr)
    ops = 0
    for i in range(1, n):
        if arr[i] <= arr[i-1]:
            diff = arr[i-1] - arr[i] + 1
            ops += diff
            arr[i] += diff
    return ops

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
