n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    subsegment = arr[l-1:r]
    is_ladder = True
    for i in range(len(subsegment)-1):
        if subsegment[i] < subsegment[i+1]:
            is_ladder = False
            break
        if subsegment[i] > subsegment[i+1]:
            break
    print("Yes" if is_ladder else "No")
