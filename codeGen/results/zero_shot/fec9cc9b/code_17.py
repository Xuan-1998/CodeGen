for _ in range(m):
    l, r = map(int, input().split())
    subsegment = arr[l:r+1]
    
    is_ladder = True
    decreasing = False
    
    for i in range(1, len(subsegment)):
        if subsegment[i] < subsegment[i-1]:
            if decreasing:
                is_ladder = False
                break
            else:
                decreasing = True
        elif subsegment[i] > subsegment[i-1]:
            if not decreasing:
                is_ladder = False
                break
            else:
                decreasing = False
    
    print("Yes" if is_ladder else "No")
