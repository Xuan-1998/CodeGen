import sys
from collections import defaultdict

def can_partition(arr):
    arr.sort()
    left = 0
    partitions = defaultdict(int)

    for i in range(len(arr)):
        while len(partitions) < (i // K + 1) and (partitions.get(arr[i], 0) or abs(arr[i] - arr[left]) > M):
            partitions[arr[left]] += 1
            left += 1

        if left == i:
            return False

    return True

n, k, m = map(int, input().split())
arr = list(map(int, (input()).split()))

print(can_partition(arr))
