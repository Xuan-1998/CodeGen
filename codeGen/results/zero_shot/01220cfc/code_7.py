Code:
def maxJump(arr):
    n = len(arr)
    lastReachableIndex = 0
    for i in range(n):
        if i > lastReachableIndex:
            return False
        lastReachableIndex = max(lastReachableIndex, i + arr[i])
    return True

import sys
n = int(input())
arr = [int(x) for x in input().split()]
print(maxJump(arr))
