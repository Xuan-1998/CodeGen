import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    subsegment = array[l-1:r]
    is_ladder = True
    for i in range(len(subsegment)-1):
        if (subsegment[i] < subsegment[i+1]):
            is_ladder = False
            break
        if (subsegment[i] > subsegment[i+1]):
            is_ladder = False
            break
    print("Yes" if is_ladder else "No")
