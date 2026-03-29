import sys

def is_ladder(arr, l, r):
    increasing = True
    decreasing = True
    
    for i in range(l-1, r):
        if arr[i] < arr[i+1]:
            decreasing = False
        elif arr[i] > arr[i+1]:
            increasing = False
            
    return increasing and not decreasing

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
queries = []
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    queries.append((l-1, r-1))

for l, r in queries:
    print('Yes' if is_ladder(arr, l, r+1) else 'No')
