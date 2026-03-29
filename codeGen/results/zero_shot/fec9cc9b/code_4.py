import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
queries = []
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    queries.append((l, r))

def is_ladder(subsegment):
    decreasing = increasing = True
    for i in range(1, len(subsegment)):
        if subsegment[i] > subsegment[i-1]:
            decreasing = False
        elif subsegment[i] < subsegment[i-1]:
            increasing = False
    return decreasing or increasing

for l, r in queries:
    print("Yes" if is_ladder(arr[l:r+1]) else "No")
