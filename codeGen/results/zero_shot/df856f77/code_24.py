import sys

def min_operations(arr):
    n = len(arr)
    result = [0] * (n + 1)

    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        if diff > 0:
            result[i] = result[i-1] + diff
        else:
            result[i] = result[i-1]

    return result[-1]

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(min_operations(arr))
