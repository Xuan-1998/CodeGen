def is_ladder(arr, l, r):
    increasing = decreasing = True
    for i in range(l, r+1):
        if arr[i] < arr[i-1]:
            increasing = False
        elif arr[i] > arr[i-1]:
            decreasing = False
    return increasing and decreasing

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
