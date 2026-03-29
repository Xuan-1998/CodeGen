def can_reach_last_index(arr):
    n = len(arr)
    i = 0
    while i < n - 1 and arr[i] > 0:
        i += min(i + arr[i], n - 1) - i
    return i == n - 1

import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(can_reach_last_index(arr))
