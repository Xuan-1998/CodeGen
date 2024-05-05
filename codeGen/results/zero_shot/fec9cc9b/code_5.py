import sys

def is_ladder(arr, l, r):
    # Check if the subsegment doesn't decrease
    for i in range(l, r+1):
        if arr[i] < arr[i-1]:
            return False
    
    # Check if the subsegment doesn't increase
    for i in range(l, r+1):
        if arr[i] > arr[i-1]:
            return False
    
    return True

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    print("Yes" if is_ladder(arr, l-1, r) else "No")
