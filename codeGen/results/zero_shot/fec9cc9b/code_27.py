import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    subseg = arr[l-1:r]
    
    is_ladder = True
    for i in range(1, len(subseg)):
        if (subseg[i] <= subseg[i-1]) or (subseg[i] >= subseg[i-1]):
            is_ladder = False
            break
    
    print("Yes" if is_ladder else "No")
