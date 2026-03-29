def is_ladder(arr, l, r):
    non_decreasing = True
    non_increasing = True
    
    for i in range(l, r+1):
        if arr[i] > arr[i-1]:
            non_decreasing = False
            break
        
    for i in range(r, l-1, -1):
        if arr[i] < arr[i-1]:
            non_increasing = False
            break
    
    return non_decreasing and non_increasing

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l-1, r-1):  # Adjust indices to 0-based
        print("Yes")
    else:
        print("No")
