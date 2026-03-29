import sys
def canReachLastIndex(arr):
    n = len(arr)
    lastReacheableIndex = n - 1
    
    for i in range(n-2, -1, -1):
        if i + arr[i] >= lastReacheableIndex:
            lastReacheableIndex = i
    return lastReacheableIndex == 0

arr = list(map(int, sys.stdin.readline().split()))
print(canReachLastIndex(arr))
