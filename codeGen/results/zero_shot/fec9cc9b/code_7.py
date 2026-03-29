import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    
    ladder = True
    for i in range(l-1, r):
        if arr[i] < arr[i+1]:
            ladder = False
            break
        if i > l-1 and arr[i] <= arr[i-1]:
            ladder = False
            break
    
    print("Yes" if ladder else "No")
