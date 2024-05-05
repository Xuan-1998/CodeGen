def is_ladder(arr, l, r):
    increasing = False
    decreasing = False
    for i in range(l, r+1):
        if arr[i] > arr[i-1]:
            increasing = True
        elif arr[i] < arr[i-1]:
            decreasing = True
    return not (increasing and decreasing)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if is_ladder(arr, l-1, r) else "No")
