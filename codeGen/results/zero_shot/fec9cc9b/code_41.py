n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    
    is_ladder = True
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:
            is_ladder = False
            break
        elif arr[i] < arr[i+1]:
            if i == l-1:
                continue  # First part of the subsegment doesn't increase
            else:
                is_ladder = False
                break

    print("Yes" if is_ladder else "No")
