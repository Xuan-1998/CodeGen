def is_ladder(arr, l, r):
    # Check if subsegment is non-decreasing
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:
            return False
    
    # Check if subsegment is non-increasing
    for i in range(l-1, r):
        if arr[i] < arr[i+1]:
            return False
    
    # If we reach here, the subsegment is a ladder
    return True

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
