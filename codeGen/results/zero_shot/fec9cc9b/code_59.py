import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    
    if arr[l-1] <= arr[r-1]:
        print("Yes")
    else:
        print("No")
