import sys

def min_operations(arr):
    n = len(arr)
    max_seen = arr[0]
    operations = 0

    for i in range(1, n):
        diff = max_seen - arr[i] + 1
        if diff > 0:
            operations += diff
        max_seen = max(max_seen, arr[i])

    return operations

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
