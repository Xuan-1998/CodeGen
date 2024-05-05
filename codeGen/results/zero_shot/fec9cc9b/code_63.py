import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    subsegment = arr[l-1:r]
    
    is_ladder = True
    for i in range(1, len(subsegment)):
        if (subsegment[i] < subsegment[i-1]) or (subsegment[i] > subsegment[0]):
            is_ladder = False
            break
    
    print("Yes" if is_ladder else "No")
