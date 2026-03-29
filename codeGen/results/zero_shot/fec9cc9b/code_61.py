n, m = map(int, input().split())
arr = list(map(int, input().split()))
subsegments = []
for _ in range(m):
    l, r = map(int, input().split())
    subsegments.append((l, r))

for l, r in subsegments:
    is_ladder = True
    decreasing = False
    increasing = False
    
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:
            decreasing = True
        elif arr[i] < arr[i+1]:
            increasing = True
            
        if decreasing and increasing:
            is_ladder = False
            break
            
    print("Yes" if is_ladder else "No")
