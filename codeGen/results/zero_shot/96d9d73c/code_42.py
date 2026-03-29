import sys

def is_possible_partition(arr):
    arr.sort()
    k = len(arr) // K  # calculate the maximum number of partitions
    for i in range(len(arr)):
        if abs(arr[i] - arr[0]) > M:  # check if the absolute difference exceeds M
            return False
        if (i + 1) % k == 0:  # new partition, check if it has at least K elements
            if len(arr[:i+1]) < K:
                return False
    return True

n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
print(is_possible_partition(arr))
