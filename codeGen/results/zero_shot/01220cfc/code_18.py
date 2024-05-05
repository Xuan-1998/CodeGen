import sys

def canReachEnd(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        if arr[i] == 0:  
            return False
        maxJump = min(i + arr[i], n - 1)  
        for j in range(max(0, i-arr[i]-1), i+1):
            if not canReachEnd(arr[:j] + [0]*maxJump):  
                return False
    return True

n = int(input())
arr = list(map(int, input().split()))
print(canReachEnd(arr))
