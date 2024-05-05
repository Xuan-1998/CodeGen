import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    subseg = arr[l-1:r]
    
    is_ladder = True
    for i in range(1, len(subseg)):
        if subseg[i-1] >= subseg[i]:
            break
    else:
        for i in range(len(subseg)-2, -1, -1):
            if subseg[i] <= subseg[i+1]:
                break
        else:
            is_ladder = False
    
    print("Yes" if is_ladder else "No")
