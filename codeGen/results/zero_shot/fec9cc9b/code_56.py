n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    subsegment = arr[l-1:r]
    is_ladder = True
    decreasing = False
    for i in range(1, len(subsegment)):
        if subsegment[i] < subsegment[i-1]:
            decreasing = True
        elif decreasing and subsegment[i] > subsegment[i-1]:
            is_ladder = False
            break
    print("Yes" if is_ladder else "No")
